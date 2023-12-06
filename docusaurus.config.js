// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const themes = require("prism-react-renderer").themes
const lightCodeTheme = themes.github
const darkCodeTheme = themes.dracula

const PRODUCTION_URL = process.env.PRODUCTION_URL || "https://integration-services.pages.aws.dev"
const BASE_URL = process.env.BASE_URL || "/eda/eda-on-aws-patterns/"

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Event-driven Architecture on AWS",
  tagline: "Enterprise-ready EDA patterns, concepts and guidance",
  favicon: "img/Res_Amazon-EventBridge_Event_48_Dark.svg",

  // Set the production url of your site here. Make sure to put the bare URL w/o the path.
  url: PRODUCTION_URL,
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: BASE_URL,

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "aws-samples",
  projectName: "eda-on-aws",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  markdown: {
    mermaid: true,
  },
  themes: ["@docusaurus/theme-mermaid"],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: "/", // Serve the docs at the site's root
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: "img/eda-social-card.png",
      navbar: {
        // title: "EDA",
        logo: {
          alt: "EDA on AWS",
          src: "img/eda-logo-colors-light.svg",
          srcDark: "img/eda-logo-colors-dark.svg",
        },
        // These are the items in the top navbar
        items: [
          {
            type: "doc",
            position: "left",
            docId: "introduction/index",
            label: "Introduction",
          },
          {
            type: "doc",
            position: "left",
            docId: "concepts/index",
            label: "Concepts",
          },
          {
            type: "doc",
            position: "left",
            docId: "patterns/index",
            label: "Patterns",
          },
          // {
          //   type: "doc",
          //   position: "left",
          //   docId: "services/index",
          //   label: "AWS Services",
          // },
          // {
          //   type: "docSidebar",
          //   sidebarId: "patternsSidebar",
          //   position: "left",
          //   label: "Patterns",
          // },
          {
            href: "https://github.com/aws-samples/eda-on-aws",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Introduction",
            items: [
              {
                label: "Introduction",
                to: "/introduction",
              },
            ],
          },
          {
            title: "Community",
            items: [
              {
                label: "Stack Overflow",
                href: "https://stackoverflow.com/search?q=%5Bamazon-web-services%5D+event-driven",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "Intro to EDA",
                href: "https://serverlessland.com/event-driven-architecture",
              },
              {
                label: "GitHub",
                href: "https://github.com/aws-samples/eda-on-aws",
              },
            ],
          },
        ],
        copyright: `Built with ❤️ at AWS<br />
          © ${new Date().getFullYear()} Amazon.com, Inc. or its affiliates. All Rights Reserved`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
}

module.exports = config
