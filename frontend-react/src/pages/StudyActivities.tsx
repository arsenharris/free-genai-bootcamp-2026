import React from 'react'
import { Link } from 'react-router-dom'

const mock = new Array(6).fill(0).map((_, i) => ({
  id: i + 1,
  title: `Activity ${i + 1}`,
  thumbnail: ''
}))

export default function StudyActivities() {
  return (
    <section>
      <h1 className="text-2xl font-semibold">Study Activities</h1>
      <div className="mt-4 grid grid-cols-3 gap-4">
        {mock.map((a) => (
          <div className="neobrutal p-4" key={a.id}>
            <div className="h-28 bg-white border border-slate-300 mb-2" />
            <div className="font-semibold">{a.title}</div>
            <div className="mt-3 flex gap-2">
              <a
                className="neo-btn"
                href={`http://localhost:8081?group_id=4`}
                target="_blank"
                rel="noreferrer"
              >
                Launch
              </a>
              <Link to={`/study-activities/${a.id}`} className="neo-btn">
                View
              </Link>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}
