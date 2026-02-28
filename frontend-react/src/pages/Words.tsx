import React from 'react'
import { Link } from 'react-router-dom'

type Word = { id: number; spanish: string; romaji: string; english: string; correct: number; wrong: number }

const mock: Word[] = new Array(50).fill(0).map((_, i) => ({
  id: i + 1,
  spanish: `palabra${i + 1}`,
  romaji: `pala${i + 1}`,
  english: `word${i + 1}`,
  correct: Math.floor(Math.random() * 10),
  wrong: Math.floor(Math.random() * 5)
}))

export default function Words() {
  return (
    <section>
      <h1 className="text-2xl font-semibold">Words</h1>
      <div className="mt-4 neobrutal p-4">
        <table className="w-full table-auto">
          <thead>
            <tr>
              <th className="text-left">Spanish</th>
              <th className="text-left">Romaji</th>
              <th className="text-left">English</th>
              <th>Correct</th>
              <th>Wrong</th>
            </tr>
          </thead>
          <tbody>
            {mock.slice(0, 50).map((w) => (
              <tr key={w.id} className="border-t">
                <td className="py-2">
                  <div className="flex items-center gap-2">
                    <button className="neo-btn">▸</button>
                    <Link to={`/words/${w.id}`} className="underline">{w.spanish}</Link>
                    <span className="text-slate-400">/ipa/</span>
                  </div>
                </td>
                <td>{w.romaji}</td>
                <td>{w.english}</td>
                <td className="text-center">{w.correct}</td>
                <td className="text-center">{w.wrong}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <div className="mt-4 flex items-center justify-between">
          <div>
            <button className="neo-btn mr-2">Previous</button>
            <span>Page <strong>1</strong> of 3</span>
            <button className="neo-btn ml-2">Next</button>
          </div>
          <div className="text-sm text-slate-500">Click headings to sort (ASC/DESC)</div>
        </div>
      </div>
    </section>
  )
}
