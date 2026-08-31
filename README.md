# MAT 274 Interactives

Hands-on activities for Differential Equations. Everything runs in your browser. Nothing to
install, no account, no Python knowledge needed.

## Open it

**https://maleygoes.github.io/diffyqinteractives**

The first load takes 20 to 60 seconds while your browser downloads the math tools. After that
it is fast. Use Chrome, Edge, Firefox, or Safari on a laptop or desktop. These do not work well
on a phone.

## New here? Start with the tour

Open **00-start-here.ipynb** first. It is a five minute walkthrough of the three things you need
to know: how to run a cell, what the output means, and what to do when something breaks. That is
the entire skill set.

## The interactives

| Notebook | Topic | Time |
| --- | --- | --- |
| `00-start-here.ipynb` | How to use these notebooks | 5 min |
| `01-slope-fields.ipynb` | Reading an ODE geometrically before solving it | 15 to 20 min |
| `02-eulers-method.ipynb` | Stepping to a numerical solution, and when it lies to you | 15 to 20 min |

More get added as we go through the semester.

## The answer checker

`check-your-answer.ipynb` is a tool rather than an activity, and it stays useful all term. Solve an
equation by hand, type your answer into it, and it tells you whether your answer actually satisfies
the equation. It works for any first-order method we cover, and it handles the answers you cannot
solve for y.

It cannot solve anything, so it is no help for doing the homework. It is a lot of help for catching
the dropped sign that would have cost you the problem. It also separates the two ways an answer goes
wrong: a formula that does not satisfy the equation at all, and a formula that does but with a
constant that misses the initial condition.

## How to work through one

Each activity is a stack of boxes called cells. Text cells explain something. Code cells make a
picture when you run them. Go top to bottom, and read the text before you run the code under it.

Most sections ask you to predict something before you run the cell. Do it. The prediction is
where the learning happens, and the picture is only feedback. Predicting wrong and finding out
why is worth more than predicting right.

Some cells have sliders. Move them slowly and watch what changes and what stays put.

## Things worth knowing

**Your changes are not saved anywhere permanent.** Notebooks live in your browser's local storage
for this browser on this computer. Clearing your history erases them. If you want to keep
something, take a screenshot or write it in your notes.

**You cannot break it.** Nothing you type here touches the real site. If a notebook gets into a
weird state, go to the Kernel menu and choose "Restart Kernel and Run All Cells."

**To get a clean copy back,** close the notebook, right click it in the file list on the left,
delete it, then refresh the page. The original comes back.

**Red error text is normal.** Usually it means a cell got run out of order. Scroll to the top and
run the cells in order from the beginning.

## Questions

Bring them to class or office hours. If something is genuinely broken on the site, email me and
say which notebook and what you clicked.

## The demos folder

`demos/` holds the sample notebooks that shipped with the software this site is built on. They
are not course material. Ignore them, or poke around if you are curious.

---

Built with [JupyterLite](https://jupyterlite.readthedocs.io). BSD 3-Clause licensed.
