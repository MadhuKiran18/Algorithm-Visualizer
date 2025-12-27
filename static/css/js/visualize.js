async function startSort() {
    const arr = document.getElementById("arrayInput").value
        .split(",")
        .map(Number);

    const algo = document.getElementById("algorithm").value;

    const res = await fetch("/sort", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ array: arr, algorithm: algo })
    });

    const steps = await res.json();
    visualize(steps);
}

function visualize(steps) {
    const container = document.getElementById("bars");
    let i = 0;

    const interval = setInterval(() => {
        container.innerHTML = "";
        steps[i].forEach(val => {
            const bar = document.createElement("div");
            bar.className = "bar";
            bar.style.height = val * 10 + "px";
            container.appendChild(bar);
        });
        i++;
        if (i >= steps.length) clearInterval(interval);
    }, 200);
}
async function startGraph() {
    const graph = JSON.parse(
        document.getElementById("graphInput").value
    );

    const start = document.getElementById("startNode").value;
    const algo = document.getElementById("graphAlgo").value;

    const res = await fetch("/graph", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            graph: graph,
            start: start,
            algorithm: algo
        })
    });

    const steps = await res.json();
    visualizeGraph(steps);
}

function visualizeGraph(steps) {
    const container = document.getElementById("graphResult");
    let i = 0;

    const interval = setInterval(() => {
        container.innerHTML =
            "<b>Visited:</b> " + steps[i].join(" → ");
        i++;
        if (i >= steps.length) clearInterval(interval);
    }, 800);
}
async function startTree() {
    const arr = document.getElementById("treeInput").value
        .split(",")
        .map(Number);

    const algo = document.getElementById("treeAlgo").value;

    const res = await fetch("/tree", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ array: arr, algorithm: algo })
    });

    const steps = await res.json();
    visualizeTree(steps);
}

function visualizeTree(steps) {
    const container = document.getElementById("treeResult");
    let i = 0;

    const interval = setInterval(() => {
        container.innerHTML =
            "<b>Traversal Order:</b> " +
            steps.slice(0, i + 1).join(" → ");
        i++;
        if (i >= steps.length) clearInterval(interval);
    }, 800);
}
async function startPathfinding() {
    const grid = JSON.parse(document.getElementById("gridInput").value);
    const start = document.getElementById("startCell").value.split(",").map(Number);
    const end = document.getElementById("endCell").value.split(",").map(Number);

    const res = await fetch("/pathfinding", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ grid, start, end })
    });

    const data = await res.json();
    drawGrid(grid, data.visited, data.path);
}

function drawGrid(grid, visited, path) {
    const container = document.getElementById("grid");
    container.innerHTML = "";

    for (let r = 0; r < grid.length; r++) {
        const row = document.createElement("div");
        for (let c = 0; c < grid[0].length; c++) {
            const cell = document.createElement("span");
            cell.className = "cell";

            if (grid[r][c] === 1) cell.classList.add("wall");
            if (visited.some(v => v[0] === r && v[1] === c)) cell.classList.add("visited");
            if (path.some(p => p[0] === r && p[1] === c)) cell.classList.add("path");

            row.appendChild(cell);
        }
        container.appendChild(row);
    }
}