import React from 'react'
import { Link, useParams } from 'react-router-dom'

export default function StudyActivityShow() {
  const { id } = useParams()

  return (
    <section>
      <h1 className="text-2xl font-semibold">Study Activity {id}</h1>
      <div className="mt-4 neobrutal p-4">
        <div className="mb-2">Thumbnail</div>
        <div className="text-lg font-bold">Activity Title</div>
        <p className="mt-2">Description placeholder</p>
        <div className="mt-3">
          <a className="neo-btn" href={`http://localhost:8081?group_id=4`} target="_blank" rel="noreferrer">Launch</a>
        </div>

        <div className="mt-6">
          <h2 className="font-semibold">Sessions</h2>
          <ul className="mt-2 space-y-2">
            <li className="p-3 neobrutal">
              <div>Group: <Link to="/groups/1" className="underline">Core Verbs</Link></div>
              <div>Start: 2026-02-24 10:00</div>
              <div>End: 2026-02-24 10:15</div>
              <div>Review Items: 15</div>
            </li>
          </ul>
        </div>
      </div>
    </section>
  )
}
