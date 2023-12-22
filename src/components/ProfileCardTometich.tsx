import React from "react"

import AWSLogo from "@site/static/img/AWS_logo_RGB.svg"
import TometichHeadshotUrl from "@site/static/img/tometich-profile.jpg"

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
        <AWSLogo className="aws-logo" width={40} />
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

        </div>
      </figcaption>
    </figure>
  )
}

export const ProfileCardTometich = () => (
  <ProfileCard
    name="Kurt Tometich"
    title="Sr. Solutions Architect"
    headshotImage={TometichHeadshotUrl}
    gitHubUsername="boomtown15"
    linkedInUsername="kurt-tometich"
    twitterUsername="boomtown15"
  ></ProfileCard>
)
