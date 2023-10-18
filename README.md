# Miniprojeto: Sistema de Gerenciamento de Eventos com HashMap

## Objetivo

O objetivo deste miniprojeto é criar um sistema de gerenciamento de eventos organizados por categorias, utilizando uma estrutura de hash map para otimizar a busca e recuperação dos eventos.

## Funcionalidades

O sistema terá as seguintes funcionalidades:

- **Inserir Evento:** O usuário pode inserir um novo evento, especificando a categoria do evento, o nome do evento e sua descrição.

- **Remover Evento:** O usuário pode remover um evento existente, informando a categoria e o nome do evento.

- **Buscar Eventos por Categoria:** O usuário pode visualizar todos os eventos de uma determinada categoria.

- **Listar Todas as Categorias:** O usuário pode listar todas as categorias de eventos disponíveis.

## Implementação

O sistema será implementado da seguinte forma:

- **Hash Map para Armazenamento:** Será utilizada uma tabela hash onde a chave será a categoria do evento e o valor será uma lista de eventos para essa categoria.

- **Operações de Inserção e Remoção:** Para inserção, será calculado o hash da categoria e o evento será inserido na lista correspondente. Para remoção, a categoria na tabela hash será encontrada e o evento será removido da lista.

- **Operação de Busca por Categoria:** O sistema calculará o hash da categoria e acessará a lista correspondente para obter todos os eventos relacionados àquela categoria.

- **Operação de Listagem de Categorias:** O sistema percorrerá a tabela hash e listará todas as categorias disponíveis.

- **Redimensionamento da tabela hash:** Quando o fator de carga da tabela hash estiver entre 0,7 e 0,8, será realizado o redimensionamento da tabela. Isso envolverá aumentar o tamanho da tabela hash para um novo tamanho apropriado (um número primo próximo ao dobro do tamanho original) e todos os elementos precisarão ser rehashed e inseridos na nova tabela.

## Restrições

1. O programa deve ser implementado em Python e deve utilizar uma estrutura de dados HashMap.

2. A implementação do TAD HashMap deve ser construída ou adaptada da implementação apresentada em sala de aula. Não devem ser utilizados componentes prontos da linguagem ou disponíveis na web.

## Equipe

| <img src="https://avatars.githubusercontent.com/u/44622004?v=4" width="250px" height="250px"> | <img src="https://avatars.githubusercontent.com/u/41112779?v=4" width="250px" height="250px"> |
| :---: | :---: |
| [Lucas Matheus ](https://github.com/Casterrr) | [Filipe Zaidan](https://github.com/filipezaidan) |

## Conteúdo consultado
- Slides do material no classroom

## Comentário sobre se conseguimos realizar ou não tudo o que foi proprosto e dificuldades encontradas 
- Conseguimos realizar todas as funcionalidades requisitadas. No início, não havíamos implementado HashMap na listagem de eventos, apenas havíamos implementado HashMap na listagem de categorias. Então repensar o código foi um desafio, mas deu certo! A maior dificuldade foi a questão do fator de carga: Criar a função do número primo mais próximo do dobro do valor e realizar a inserção de cada categoria e eventos cadastrados na nova tabela de tamanho maior... Bugou bastante kkkk, mas foi!


