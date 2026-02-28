import React from 'react'
import { Link } from 'react-router-dom'

const groups = new Array(10).fill(0).map((_, i) => ({ id: i + 1, name: `Group ${i + 1}`, words: 10 + i }))

export default function Groups(){
  return (
    <section>
      <h1 className="text-2xl font-semibold">Word Groups</h1>
      <div className="mt-4 neobrutal p-4">
        <table className="w-full">
          <thead>
            <tr>
              <th className="text-left">Group Name</th>
              <th className="text-left">Words</th>
            </tr>
          </thead>
          <tbody>
            {groups.map(g => (
              <tr key={g.id} className="border-t">
                <td className="py-2"><Link to={`/groups/${g.id}`} className="underline">{g.name}</Link></td>
                <td>{g.words}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}
