import React from "react"
import clsx from "clsx"
import styles from "./styles.module.css"

type FeatureItem = {
  title: string
  Svg: React.ComponentType<React.ComponentProps<"svg">>
  description: JSX.Element
}

const FeatureList: FeatureItem[] = [
  {
    title: "Speed & Agility",
    Svg: require("@site/static/img/speed-svgrepo-com.svg").default,
    description: <>Move faster. Build and deploy services independently.</>,
  },
  {
    title: "Resiliency",
    Svg: require("@site/static/img/confidence-confident-dignity-svgrepo-com.svg").default,
    description: (
      <>
        Eliminate or drastically reduce cascading failures. Loosely coupled systems can run and fail
        independently.
      </>
    ),
  },
  {
    title: "Scalability",
    Svg: require("@site/static/img/scale-svgrepo-com.svg").default,
    description: <>Minimize waiting time through async and parallel processing.</>,
  },
]

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  )
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  )
}
