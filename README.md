# EDA on AWS Patterns

This is the source for [EDA Patterns on AWS](https://aws-samples.github.io/eda-on-aws/). We welcome
contributions, bug fixes, suggestions and improvements.

Please read our [CODE_OF_CONDUCT](/CODE_OF_CONDUCT.md) and [CONTRIBUTING](/CONTRIBUTING.md) before
submitting your contributions.

If you have suggestion for content or general feedback, please open a [new GitHub issue](/issues).

## EDA Topics

The contents are split into three major categories:

- Concepts: Fundamental ideas/concepts that are applicable to EDA and distributed systems in
  general.
- Patterns: Popular EDA patterns that people hear/read about
- EventStorming: Explaining fundamentals of the EventStorming process, and how it's useful when
  designing EDAs.

The primary goal of this content is to offer clear explanations and guidance on fundamental and
sometimes confusing event-driven architecture topics and patterns.

### Concepts

- Idempotency/handling duplicates [COMPLETE]
  - Author: Brian Zambrano
- Message ordering [COMPLETE]
  - Author: Brian Zambrano
- Event/schema evolution/versioning [NOT STARTED]

### EDA Patterns

- Event Sourcing [COMPLETE]
  - Author: Kurt Tometich
- Saga [COMPLETE]
  - Author: Jordi Macià
- Claim check [IN PROGRESS]
  - Authors: Rodrigo Cabrera/Rogelio Ramirez Rubio
- CQRS [NOT STARTED]
- Projections/materialized views [NOT STARTED]
- Error Callback from consumer [NOT STARTED]

### EventStorming

- Big Picture [COMPLETE]
  - Owner: Brian Zambrano

## Local build/development

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website
generator.

These commands install dependencies, starts a local development server, and opens up a browser
window. Most changes are reflected live without having to restart the server.

```bash
npm i
npm run start
```

The `npm run start` command builds the website locally and serves it through a development server,
ready for you to view at http://localhost:3000/.

## Repo structure

Content for the EDA topics live in the `/docs` directory. The sub-directories are prefixed with
`01-, 02-, etc.` as a convention to sort the content in the menu/navigation.

To start a new topic, create a new folder with an incremented prefix (i.e., `03-mytopic`), create a
new `index.mdx` file, and start writing.

MDX is a flavor of Markdown that allows you to embed/use JSX components. See the ordering an
idempotency `index.mdx` files for examples on how to take advantage of that.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License Summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0
International License. See the LICENSE file.

The sample code within this documentation is made available under the MIT-0 license. See the
LICENSE-SAMPLECODE file.
