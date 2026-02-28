import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { NavBar } from './components/NavBar'
import { Breadcrumbs } from './components/Breadcrumbs'
import Dashboard from './pages/Dashboard'
import StudyActivities from './pages/StudyActivities'
import StudyActivityShow from './pages/StudyActivityShow'
import Words from './pages/Words'
import WordShow from './pages/WordShow'
import Groups from './pages/Groups'
import GroupShow from './pages/GroupShow'
import Sessions from './pages/Sessions'
import Settings from './pages/Settings'
import NotFound from './pages/NotFound'

export default function App() {
  return (
    <div className="min-h-screen bg-nbg text-slate-900 p-6">
      <NavBar />
      <div className="mt-4">
        <Breadcrumbs />
      </div>

      <main className="mt-6">
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/study-activities" element={<StudyActivities />} />
          <Route path="/study-activities/:id" element={<StudyActivityShow />} />
          <Route path="/words" element={<Words />} />
          <Route path="/words/:id" element={<WordShow />} />
          <Route path="/groups" element={<Groups />} />
          <Route path="/groups/:id" element={<GroupShow />} />
          <Route path="/session" element={<Sessions />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </div>
  )
}
