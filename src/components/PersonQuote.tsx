import React from "react"

export const PersonQuote = ({ children, author, url }) => {
  return (
    <blockquote>
      <span className="person-quote">{children}</span>
      {author && (
        <span className="quote-author">
          <i>‒{author}</i>
        </span>
      )}
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
