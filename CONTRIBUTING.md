# Como contribuir com o Ingenium

Antes de mudar o projeto, consulte [STATUS.md](docs/STATUS.md) para entender o objetivo atual, [ARCHITECTURE.md](docs/ARCHITECTURE.md) para ver como o código funciona e [PRINCIPLES.md](docs/PRINCIPLES.md) para conhecer os critérios de desenvolvimento. Parta de `main` atualizada e use uma branch própria para a alteração.

## Preparar e executar o projeto

Instale a versão do uv declarada em [`pyproject.toml`](pyproject.toml). No PowerShell, execute os comandos abaixo a partir da raiz do repositório.

```powershell
uv --version
uv sync --locked
uv run --locked python --version
uv run --locked python src/main.py
uv run --locked pytest
```

`uv sync --locked` prepara a `.venv` com as versões registradas em `uv.lock` e falha se o arquivo precisar ser atualizado. `uv run --locked` executa o comando no ambiente do projeto. Compare a versão do Python exibida com [`.python-version`](.python-version). A CLI abre com `Ingenium ready.` e fecha com `exit` ou quando a entrada termina.

## Alterar código, testes ou documentação

| Se você quer… | Onde trabalhar |
| --- | --- |
| Mudar o comportamento do terminal | Use [`src/main.py`](src/main.py) como ponto de partida. Confira como a alteração afeta o prompt, as entradas vazias e o encerramento da sessão. |
| Adicionar uma funcionalidade | Implemente em `src/`. Se a mudança trouxer uma responsabilidade distinta da leitura e da exibição no terminal, mantenha essa lógica separada do loop. Inclua um teste de caso base. |
| Corrigir um comportamento | Reproduza o problema e use os testes para verificar a correção. [`tests/test_cli.py`](tests/test_cli.py) já mostra como enviar comandos ao programa em um subprocesso e conferir a saída. |
| Atualizar a documentação | Use `README.md` para a visão geral e as instruções de execução, `docs/ARCHITECTURE.md` para o que está implementado, `docs/STATUS.md` para o progresso e o próximo passo e `docs/DECISIONS.md` para decisões confirmadas. |

## Gerenciar dependências com uv

Use `uv add` para bibliotecas usadas pelo programa e `uv add --dev` para ferramentas de desenvolvimento, como as usadas pelos testes. Nos exemplos, substitua `nome-do-pacote` pelo pacote escolhido.

| Alteração | Comando |
| --- | --- |
| Adicionar dependência do programa | `uv add nome-do-pacote` |
| Adicionar dependência de desenvolvimento | `uv add --dev nome-do-pacote` |
| Remover dependência do programa | `uv remove nome-do-pacote` |
| Remover dependência de desenvolvimento | `uv remove --dev nome-do-pacote` |
| Atualizar um pacote dentro das restrições declaradas | `uv lock --upgrade-package nome-do-pacote` |

Ao mudar uma restrição de versão em `pyproject.toml`, rode `uv lock` para atualizar a resolução. Revise o diff, rode `uv sync --locked` e `uv run --locked pytest` e inclua no commit as alterações em `pyproject.toml` e `uv.lock` que resultarem da mudança. A `.venv` é local e já está no `.gitignore`.

## Versionar a alteração e abrir a PR

O Git registra as alterações do projeto. Faça commits com mudanças relacionadas e mensagens que descrevam o que mudou. A versão do projeto fica em `[project].version` no `pyproject.toml`. A versão de referência do Python fica em `.python-version`, a faixa aceita em `[project].requires-python` e a versão exigida do uv em `[tool.uv].required-version`. Se a contribuição alterar Python ou uv, confira também as referências no README e na CI e valide o ambiente com as versões propostas.

Antes de abrir a PR para `main`, revise o diff e rode `uv run --locked pytest`. Preencha o [modelo de PR](.github/pull_request_template.md) com o objetivo, os critérios de aceite verificáveis, o escopo e as decisões confirmadas. Use o resultado da CI no GitHub para conferir a execução no Windows.
