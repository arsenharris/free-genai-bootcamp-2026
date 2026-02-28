import React from 'react'
import { useParams } from 'react-router-dom'

export default function WordShow() {
  const { id } = useParams()

  return (
    <section>
      <h1 className="text-2xl font-semibold">Word {id}</h1>
      <div className="mt-4 neobrutal p-4">
        <div className="text-lg font-bold">palabra{ id }</div>
        <div className="mt-2">Romaji: pala{ id }</div>
        <div>English: word{ id }</div>
      </div>
    </section>
  )
}
