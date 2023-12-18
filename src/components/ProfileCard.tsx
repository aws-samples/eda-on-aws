import React from "react"

import BrianHeadshotUrl from "@site/static/img/bz-hiking.jpeg"
import JomafeHeadshotUrl from "@site/static/img/jomafe_photo.jpg"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faLinkedin, faTwitter, faGithub } from "@fortawesome/free-brands-svg-icons"

const ProfileCard = ({
  name,
  title,
  headshotImage,
  linkedInUsername,
  twitterUsername,
  gitHubUsername,
}) => {
  return (
    <figure className="profile-card">
      <div className="profile-image">
        <img src={headshotImage} alt={`${name}, ${title}`} />
      </div>
      <figcaption>
        <h3>{name}</h3>
        <h5>{title}</h5>
        <div className="icons">
          {linkedInUsername && (
            <a href={`https://www.linkedin.com/in/${linkedInUsername}/`} target="_new">
              <FontAwesomeIcon icon={faLinkedin} />
            </a>
          )}
          {gitHubUsername && (
            <a href={`https://github.com/${gitHubUsername}`} target="_new">
              <FontAwesomeIcon icon={faGithub} />
            </a>
          )}
          {twitterUsername && (
            <a href={`https://twitter.com/${twitterUsername}`} target="_new">
              <FontAwesomeIcon icon={faTwitter} />
            </a>
          )}
        </div>
      </figcaption>
    </figure>
  )
}

export const BrianProfileCard = () => (
  <ProfileCard
    name="Brian Zambrano"
    title="Sr. Specialist Solutions Architect, Serverless"
    headshotImage={BrianHeadshotUrl}
    gitHubUsername="brianz"
    linkedInUsername="brianzambrano"
    twitterUsername="brianzambrano"
  ></ProfileCard>
)

export const JomafeProfileCard = () => (
  <ProfileCard
    name="Jordi Macià"
    title="Sr. Solutions Architect, CPG"
    headshotImage={JomafeHeadshotUrl}
    gitHubUsername="jomafe"
    linkedInUsername="jordimacia"
    twitterUsername=""
  ></ProfileCard>
)