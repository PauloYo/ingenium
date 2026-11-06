# Revisor automático de PRs

Cada PR recebe um relatório (`review.md`) gerado pelo Claude Code no GitHub
Actions. O relatório é consultivo: quem decide, corrige e faz merge é o Paulo.

| Arquivo | Papel |
|---------|-------|
| `.github/pull_request_template.md` | Entrada da revisão: marco, critérios de aceite, fora do escopo, decisões confirmadas. |
| `.github/pr-review/instructions.md` | Instruções versionadas do revisor e formato do relatório. |
| `.github/workflows/pr-review.yml` | Orquestra contexto, CI e revisão. |
| `.github/workflows/ci.yml` | CI do projeto (G0), reaproveitada pela revisão via `workflow_call`. |

## Como funciona

```text
PR aberta / reaberta / novo commit  (ou execução manual com o número da PR)
  │
  ├─ context  resolve PR, SHA exato e se a revisão com credencial é permitida
  │
  ├─ ci       roda .github/workflows/ci.yml nesse SHA (Windows, sem secrets)
  │
  └─ review   roda mesmo se a CI falhar
              ├─ prepara entradas: pr.json, pr-body.md, pr.diff, ci-results.md
              ├─ Claude lê docs/ + entradas, escreve o relatório e,
              │  se houver atualização concreta, edita docs/
              ├─ workflow monta review.md (cabeçalho com PR, SHA e CI)
              │  e gera docs.patch a partir das edições em docs/
              └─ publica o artefato review-pr-<número>-<sha>
```

- **SHA:** CI e revisão usam o mesmo `head.sha` da PR. O SHA aparece no nome
  do artefato e no cabeçalho do `review.md`.
- **CI com falha:** o job `review` usa `always()`, recebe passos, conclusões e
  o final dos logs da CI, e o relatório é publicado mesmo assim.
- **Falha do Claude:** o `review.md` é publicado com a seção "Falha da revisão"
  e os resultados da CI, e o job `review` termina em vermelho.
- **docs.patch:** só contém mudanças em `docs/`, só é publicado se a revisão
  terminou bem e se `git apply --check` passou contra o SHA revisado. Nada é
  commitado nem enviado à PR.

## Segurança

- **Quem aciona a credencial:** o job `review` só roda quando a branch da PR é
  deste repositório e o autor é `OWNER`, `MEMBER` ou `COLLABORATOR`. PRs de
  forks e de outros autores continuam rodando o job `ci`, sem secret.
- **Evento:** usa `pull_request`, nunca `pull_request_target`. O código da PR
  não roda num contexto privilegiado.
- **Permissões mínimas:** o workflow começa com `permissions: {}`. O `ci` tem
  `contents: read` e não recebe secrets. O `review` tem `contents: read`,
  `pull-requests: read` e `actions: read` (para ler os resultados da CI).
- **Sem GitHub App:** o Claude recebe o `GITHUB_TOKEN` somente leitura do
  próprio workflow. Ele não consegue comentar, fazer push nem merge.
- **Entradas como dados:** título, corpo e diff da PR vão para arquivos, nunca
  para comandos do shell. As instruções mandam tratá-los como dados e
  registrar tentativas de instrução como achado. O Claude roda sem `Bash` e
  sem acesso à web (`--allowedTools "Read,Glob,Grep,Write,Edit"`).
- **Limite conhecido:** no evento `pull_request` o GitHub executa o workflow e
  as instruções da própria branch da PR. Por isso a credencial fica restrita a
  autores com acesso de escrita, que já poderiam alterar esses arquivos.

## Configuração no GitHub (uma vez)

1. **Credencial.** Em *Settings → Secrets and variables → Actions → New
   repository secret*, crie **um** destes:
   - `ANTHROPIC_API_KEY`: chave de API do Console da Anthropic
     (cobrança por uso); ou
   - `CLAUDE_CODE_OAUTH_TOKEN`: token da sua assinatura Claude, gerado com
     `claude setup-token` no terminal.
2. **Permissões do Actions.** Em *Settings → Actions → General*:
   - *Workflow permissions*: **Read repository contents and packages
     permissions** (o workflow pede o resto explicitamente).
   - *Fork pull request workflows*: mantenha a aprovação exigida para
     contribuidores externos.
3. **GitHub App do Claude:** não é necessário para este workflow.

## Onde baixar o relatório

1. Abra a PR → aba *Checks* → execução **PR Review** (ou *Actions → PR Review*
   → a execução da PR).
2. Na página da execução, role até **Artifacts** e baixe
   `review-pr-<número>-<sha>`. O zip contém:
   - `review.md`: o relatório;
   - `ci-results.md`: passos e logs da CI usados na revisão;
   - `docs.patch`: só quando houver atualização de documentação proposta.

O resumo da execução (*Summary*) mostra o nome do artefato, se a revisão
terminou e se há `docs.patch`. Os artefatos ficam 30 dias.

## Aplicar o docs.patch

Na raiz do repositório, com a branch da PR em checkout no mesmo SHA do
relatório:

```powershell
git rev-parse HEAD                      # deve ser o SHA do review.md
git apply --check caminho\docs.patch    # só verifica, não altera nada
git apply caminho\docs.patch            # aplica no working tree
git diff -- docs/                       # revise antes de commitar
```

Se o `--check` falhar, a branch mudou depois da revisão: rode a revisão de novo
no SHA atual.

## Rodar de novo

- **Novo commit na PR:** roda sozinho (`synchronize`).
- **Mesmo SHA:** na execução, *Re-run jobs* (todos ou só os falhos). O artefato
  é sobrescrito.
- **Diagnóstico manual:** *Actions → PR Review → Run workflow*, informando o
  número da PR. Usa o commit mais recente dela, pela mesma lógica.

## Testar com a primeira PR

1. Configure o secret (passo 1 acima).
2. Faça commit destes arquivos numa branch e abra a PR preenchendo o template.
3. Confira na aba *Checks*: `context`, `ci / smoke-test` e `review`.
4. Baixe o artefato e confira: SHA do cabeçalho igual ao último commit da PR,
   critérios com status e evidência, testes listados.
5. Opcional: teste o caminho de falha com um commit temporário que quebre a
   saída de `src/main.py`. A CI deve falhar e o `review.md` ainda deve sair,
   apontando o passo que falhou.

## Versões fixadas

Toda ação é fixada pelo SHA do commit, com a tag em comentário:

| Ação | Tag | Usada em |
|------|-----|----------|
| `actions/checkout` | v7.0.1 | ci.yml, pr-review.yml |
| `astral-sh/setup-uv` | v9.0.0 | ci.yml |
| `actions/upload-artifact` | v7.0.2 | pr-review.yml |
| `anthropics/claude-code-action` | v1.0.268 | pr-review.yml |

O Claude Code que roda na revisão é instalado pela própria
`claude-code-action`. Atualizar a action pode trazer uma versão nova dele, por
isso a atualização merece uma PR própria.

Para atualizar uma ação:

1. Leia as notas de versão no GitHub da ação (mudanças de inputs, permissões
   ou runtime).
2. Descubra o SHA do commit da nova tag. Para tags anotadas, use a linha com
   `^{}`:

   ```bash
   git ls-remote --tags https://github.com/anthropics/claude-code-action 'refs/tags/v1.0.300*'
   ```

3. Troque o SHA e o comentário `# vX.Y.Z` em todos os workflows que usam a
   ação e atualize a tabela acima.
4. Abra uma PR só com essa atualização e confira que `ci` e `review` passam.
