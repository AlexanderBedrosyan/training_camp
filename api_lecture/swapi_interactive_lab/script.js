const taskListEl = document.getElementById('task-list');
const taskTitleEl = document.getElementById('task-title');
const outputEl = document.getElementById('output');
const statusBadgeEl = document.getElementById('status-badge');
const taskMetaEl = document.getElementById('task-meta');
const runButton = document.getElementById('run-task-btn');

let tasks = [];
let selectedTaskId = 1;

async function loadTasks() {
  const response = await fetch('/api/tasks');
  const data = await response.json();
  tasks = data.tasks || [];

  if (!tasks.length) {
    outputEl.textContent = 'No tasks were loaded.';
    return;
  }

  renderTaskList();
  setSelectedTask(tasks[0].id);
}

function renderTaskList() {
  taskListEl.innerHTML = '';

  tasks.forEach((task) => {
    const item = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'task-item';

    if (task.id === selectedTaskId) {
      button.classList.add('selected');
    }

    button.innerHTML = `
      <strong>Task ${task.id}</strong>
      <small>${task.title}</small>
    `;

    button.addEventListener('click', () => setSelectedTask(task.id));
    item.appendChild(button);
    taskListEl.appendChild(item);
  });
}

async function setSelectedTask(taskId) {
  selectedTaskId = Number(taskId);
  const task = tasks.find((item) => item.id === selectedTaskId);

  if (!task) {
    return;
  }

  renderTaskList();
  taskTitleEl.textContent = `Task ${task.id}: ${task.title}`;
  taskMetaEl.textContent = `${task.category} / ${task.difficulty}`;
  statusBadgeEl.textContent = 'Loading...';
  outputEl.textContent = 'Requesting data from SWAPI...';

  try {
    const response = await fetch(`/api/task/${task.id}`);
    const payload = await response.json();
    outputEl.textContent = JSON.stringify(payload, null, 2);
    statusBadgeEl.textContent = payload.status === 'starter' ? 'Starter' : 'Ready';
  } catch (error) {
    outputEl.textContent = `Error while fetching data:\n${error.message}`;
    statusBadgeEl.textContent = 'Error';
  }
}

runButton.addEventListener('click', () => setSelectedTask(selectedTaskId));

loadTasks();
