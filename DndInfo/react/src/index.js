import React from 'react'

const ResultsList = ({results, searchType}) => {
    
      return (
        <>
            {results.map((result) => [
                searchType == 'card' ? renderCard(result) : renderSet(result)
            ])}
        </>
      );

  }
  let renderCard = (result) =>{
    return(
        <div className="card">
            {result.fields.name}
            {result.fields.mana_cost}
            {result.fields.text}
        </div>
    )
  }
  let renderSet = (result) =>{
    return(
        <div className ="card">
            {result.fields.name}
            {result.fields.block}
            {result.fields.code}
        </div>
    )
  }
  
export default ResultsList