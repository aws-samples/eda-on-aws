import React from "react"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faLinkedin, faTwitter, faGithub } from "@fortawesome/free-brands-svg-icons"
import useBaseUrl from "@docusaurus/useBaseUrl"

const AuthorProfile = (author) => (
  <span>
    <div className="profile-image">
      <img src={useBaseUrl(author.headshotImage)} alt={`${author.name}, ${author.title}`} />
    </div>
    <figcaption>
      <h3>{author.name}</h3>
      <h5>{author.title}</h5>
      <div className="icons">
        {author.linkedInUsername && (
          <a href={`https://www.linkedin.com/in/${author.linkedInUsername}/`} target="_new">
            <FontAwesomeIcon icon={faLinkedin} />
          </a>
        )}
        {author.gitHubUsername && (
          <a href={`https://github.com/${author.gitHubUsername}`} target="_new">
            <FontAwesomeIcon icon={faGithub} />
          </a>
        )}
        {author.twitterUsername && (
          <a href={`https://twitter.com/${author.twitterUsername}`} target="_new">
            <FontAwesomeIcon icon={faTwitter} />
          </a>
        )}
      </div>
    </figcaption>
  </span>
)

const ProfileCard = ({ authors }) => {
  return <figure className="profile-card">{authors.map(AuthorProfile)}</figure>
}

/**
 *
 Add author profile cards here
 *
*/

export const BrianProfileCard = () => {
  const author = {
    name: "Brian Zambrano",
    title: "Sr. Specialist Solutions Architect, Serverless",
    headshotImage: "/img/bz-hiking.jpeg",
    gitHubUsername: "brianz",
    linkedInUsername: "brianzambrano",
    twitterUsername: "brianzambrano",
  }
  return <ProfileCard authors={[author]} />
}

export const JomafeProfileCard = () => {
  const author = {
    name: "Jordi Macià",
    title: "Sr. Solutions Architect, CPG",
    headshotImage: "/img/jomafe_photo.jpg",
    gitHubUsername: "jomafe",
    linkedInUsername: "jordimacia",
  }
  return <ProfileCard authors={[author]} />
}

export const ProfileCardTometich = () => {
  const author = {
    name: "Kurt Tometich",
    title: "Sr. Solutions Architect",
    headshotImage: "/img/tometich-profile.jpg",
    gitHubUsername: "boomtown15",
    linkedInUsername: "kurt-tometich",
    twitterUsername: "boomtown15",
  }

  return <ProfileCard authors={[author]} />
}

export const RodrigoRogelioProfileCard = () => {
  const rodcab = {
    name: "Rodrigo Cabrera",
    title: "Sr. Solutions Architect",
    headshotImage: "/img/rodcab_badge.jpg",
    gitHubUsername: "rodcab1",
    linkedInUsername: "rodrigo-cabrera-pliego-75455755",
    twitterUsername: "Rodrigo11033869",
  }
  const rogelio = {
    name: "Rogelio Ramirez",
    title: "Solutions Architect",
    headshotImage: "/img/photo_rogelio.jpg",
    linkedInUsername: "rogelio-ramirez-rubio",
  }
  return <ProfileCard authors={[rodcab, rogelio]} />
}

export const EventSourcingProfileCard = () => {
  const doug = {
    name: "Doug Perkes",
    title: "Sr. Solutions Architect",
    headshotImage: "/img/dougperkes-badge.jpeg",
    gitHubUsername: "dougperkes",
    linkedInUsername: "dougperkes",
    twitterUsername: "dougperkes",
  }
  const rajdeep = {
    name: "Rajdeep Banerjee",
    title: "Sr. Solutions Architect",
    headshotImage: "/img/rajdeep-banerjee-badge.jpeg",
    linkedInUsername: "rajdeep-banerjee",
    gitHubUsername: "rajdban",
  }
  const kurt = {
    name: "Kurt Tometich",
    title: "Sr. Solutions Architect",
    headshotImage: "/img/tometich-profile.jpg",
    gitHubUsername: "boomtown15",
    linkedInUsername: "kurt-tometich",
    twitterUsername: "boomtown15",
  }
  const james = {
    name: "James Eastham",
    title: "Sr. Solutions Architect",
    headshotImage: "/img/james-eastham-profile.png",
    linkedInUsername: "james-eastham",
    twitterUsername: "plantpowerjames",
    gitHubUsername: "jeastham1993"
  }
  return <ProfileCard authors={[doug, kurt, rajdeep, james]} />
}
