import React from "react"

export const Quote = ({ children, url }) => {
  return (
    <blockquote>
      <span className="person-quote">{children}</span>
      {url && (
        <div className="quote-ref">
          <a href="{url}">
            <i>{url}</i>
          </a>
        </div>
      )}
    </blockquote>
  )
}

export const PersonQuote = ({ children, author, url }) => {
  return (
    <blockquote>
      <span className="person-quote">{children}</span>
      <span className="quote-author">
        <i>‒{author}</i>
      </span>
      {url && (
        <div className="quote-ref">
          <a href="{url}">
            <i>{url}</i>
          </a>
        </div>
      )}
    </blockquote>
  )
}
