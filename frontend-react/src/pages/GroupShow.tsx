import React from 'react'
import { useParams } from 'react-router-dom'

export default function GroupShow(){
  const { id } = useParams()

  return (
    <section>
      <h1 className="text-2xl font-semibold">Group {id}</h1>
      <div className="mt-4 neobrutal p-4">Words scoped to this group (placeholder)</div>
    </section>
  )
}
