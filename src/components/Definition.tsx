import React from "react"

export const Definition = ({ term, wordType, children }) => {
  const containerStyle = {
    backgroundColor: "#fff",
    border: "1px solid #ccc",
    borderRadius: "10px",
    boxShadow: "0 2px 5px rgba(0, 0, 0, 0.1)",
    maxWidth: "640px",
    padding: "20px",
    marginBottom: "20px",
  }

  const headingStyle = {
    color: "#333",
    marginBottom: "10px",
  }

  const listStyle = {
    color: "#333",
    lineHeight: "1.6",
    marginBottom: "0",
  }

  return (
    <div className="definition-container" style={containerStyle}>
      <h2 style={headingStyle}>{term}</h2>
      <h4>{wordType}</h4>
      <ol style={listStyle}>
        {React.Children.map(children, (child, index) => (
          <li key={index}>{child}</li>
        ))}
      </ol>
    </div>
  )
}
