import { Component } from '@angular/core';

@Component({
  selector: 'app-taskflow-demo',
  template: `
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Task Management Dashboard</h1>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="bg-white shadow rounded-lg p-4">
          <h2 class="text-xl font-semibold">Tasks Overview</h2>
          <p class="text-gray-600">Your daily task overview</p>
          <button class="bg-blue-500 text-white px-4 py-2 rounded mt-2">Add Task</button>
        </div>
        <div class="bg-white shadow rounded-lg p-4">
          <h2 class="text-xl font-semibold">In Progress</h2>
          <ul>
            <li class="border-b py-2">Task A</li>
            <li class="border-b py-2">Task B</li>
          </ul>
        </div>
        <div class="bg-white shadow rounded-lg p-4">
          <h2 class="text-xl font-semibold">Completed</h2>
          <ul>
            <li class="border-b py-2">Task C</li>
            <li class="border-b py-2">Task D</li>
          </ul>
        </div>
      </div>
    </div>
  `,
  styles: []
})
export class TaskflowDemoComponent {}
