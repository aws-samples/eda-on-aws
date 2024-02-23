import React from "react"

export const PersonQuote = ({ children, author, url }) => {
  return (
    <blockquote>
      <div>
        <p className="person-quote">&#8220;{children}&#8221;</p>
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
      </div>
    </blockquote>
  )
}
