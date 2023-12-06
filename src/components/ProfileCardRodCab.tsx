import React from "react"

import RodrigoHeadshotUrl from "@site/static/img/rodcab_badge.jpg"
import RogelioHeadshotUrl from "@site/static/img/photo_rogelio.jpg"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faLinkedin, faTwitter, faGithub } from "@fortawesome/free-brands-svg-icons"

const ProfileCard = ({
  name,
  title,
  headshotImage,
  linkedInUsername,
  twitterUsername,
  gitHubUsername,
  name2,
  title2,
  headshotImage2,
  linkedInUsername2,
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
      <div className="profile-image">
        <img src={headshotImage2} alt={`${name2}, ${title2}`} />
      </div>
      <figcaption>
        <h3>{name2}</h3>
        <h5>{title2}</h5>
        <div className="icons">
          {linkedInUsername && (
            <a href={`https://www.linkedin.com/in/${linkedInUsername2}/`} target="_new">
              <FontAwesomeIcon icon={faLinkedin} />
            </a>
          )}
        </div>
      </figcaption>
    </figure>
  )
}

export const RodrigoProfileCard = () => (
  <ProfileCard
    name="Rodrigo Cabrera"
    title="Sr. Solutions Architect"
    headshotImage={RodrigoHeadshotUrl}
    gitHubUsername="rodcab1"
    linkedInUsername="rodrigo-cabrera-pliego-75455755"
    twitterUsername="Rodrigo11033869"
    name2="Rogelio Ramirez"
    title2="Solutions Architect"
    headshotImage2={RogelioHeadshotUrl}
    linkedInUsername2="rogelio-ramirez-rubio"
  ></ProfileCard>
)
