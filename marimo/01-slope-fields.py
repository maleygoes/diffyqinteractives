# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "numpy",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Slope Fields")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Slope Fields: Seeing an ODE Before Solving It

        **Time:** about 15 to 20 minutes.
        **You need:** nothing but this page.

        A first-order differential equation

        $$\frac{dy}{dt}=f(t,y)$$

        does not hand you the value of $y$. What it hands you is a rule for the *slope*: at every
        point $(t,y)$ in the plane, it tells you how steeply a solution passing through that point
        would be climbing or falling.

        So before you solve anything, you can go to every point and draw a tiny segment at the slope
        the equation demands there. That picture is a **slope field**.

        > **The main idea:** a solution curve is a path that follows the little segments.

        Everything in this activity is a consequence of that one sentence.

        Each section asks you to predict before you look. Make the prediction out loud or on paper
        first. Getting it wrong and seeing why is the point.

        /// tip | This is a marimo notebook
        There is nothing to install and nothing to run. Where a section asks you to predict
        something, the picture stays hidden behind a **Show** switch until you flip it, so make the
        prediction first. Once a picture is showing, any slider under it redraws the plot live as
        you drag.
        ///
        """
    )
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import marimo as mo
    return mo, np, plt


@app.cell
def _(np, plt):
    def slope_field(f, t_range=(-3, 3), y_range=(-3, 3), density=21,
                    solutions=None, title=None):
        """Draw the slope field for y prime = f(t, y), optionally with solution curves."""
        t = np.linspace(*t_range, density)
        y = np.linspace(*y_range, density)
        T, Y = np.meshgrid(t, y)
        M = f(T, Y)

        # Normalize the segments so steep slopes don't dominate the picture.
        U = 1 / np.sqrt(1 + M**2)
        V = M / np.sqrt(1 + M**2)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.quiver(T, Y, U, V, angles='xy', pivot='middle', color='0.35',
                  headlength=0, headwidth=0, headaxislength=0)
        ax.axhline(0, color='0.6', linewidth=0.8)
        ax.axvline(0, color='0.6', linewidth=0.8)
        ax.set_xlim(t_range)
        ax.set_ylim(y_range)
        ax.set_xlabel('t')
        ax.set_ylabel('y')
        ax.set_title(title or "slope field for y' = f(t, y)")
        ax.grid(alpha=0.2)

        if solutions:
            for i, (ts, ys, label) in enumerate(solutions):
                ax.plot(ts, ys, linewidth=2.5, label=label,
                        color=f'C{i}', linestyle=['-', '--', '-.', ':'][i % 4])
            ax.legend(loc='upper left', framealpha=0.9)

        return fig


    def trace(f, t0, y0, t_range=(-3, 3), steps=600):
        """Follow the slope field from (t0, y0) in both directions. Returns (ts, ys)."""
        def march(t_start, t_end):
            n = max(int(steps * abs(t_end - t_start) / 6), 2)
            h = (t_end - t_start) / n
            ts, ys = [t_start], [y0]
            t, y = t_start, y0
            for _ in range(n):
                k1 = f(t, y)
                k2 = f(t + h/2, y + h*k1/2)
                k3 = f(t + h/2, y + h*k2/2)
                k4 = f(t + h, y + h*k3)
                y = y + h*(k1 + 2*k2 + 2*k3 + k4)/6
                t = t + h
                ts.append(t); ys.append(y)
            return ts, ys

        tb, yb = march(t0, t_range[0])
        tf, yf = march(t0, t_range[1])
        ts = np.array(tb[::-1] + tf[1:])
        ys = np.array(yb[::-1] + yf[1:])
        return ts, ys
    return slope_field, trace


@app.cell
def _(mo):
    def gated(switch, draw,
              hint="Make your prediction first, then flip the switch above."):
        """Keep a picture hidden until the switch is flipped, so prediction comes first."""
        if switch.value:
            return draw()
        return mo.callout(mo.md(hint), kind="info")
    return (gated,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 1. First look: what does $y'=y$ mean?

        Read the equation

        $$y'=y$$

        as a sentence: *the slope equals the height*. That is all it says.

        Before you look at the picture, predict:

        - What do the slopes look like where $y > 0$?
        - What about where $y < 0$?
        - What happens along the line $y = 0$?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    see_exponential = mo.ui.switch(
        value=False, label="Show the slope field for $y'=y$")
    see_exponential
    return (see_exponential,)


@app.cell(hide_code=True)
def _(gated, see_exponential, slope_field):
    gated(see_exponential,
          lambda: slope_field(lambda t, y: y, title="y' = y"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Check your intuition

        Look across any *horizontal* row of the picture. The segments in that row are all parallel.

        That is not a coincidence. Since $y'=y$ depends only on $y$ and not on $t$, every point at
        the same height gets the same slope, no matter how far left or right you go.

        **In your notes:** in one sentence, why are the segments flat at $y=0$, tilted up above it,
        and tilted down below it?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Check yourself after you have written something": mo.md(
                r"""
                Because the slope *is* the height. At $y=0$ the equation demands slope $0$, so the
                segments are flat. At $y=2$ it demands slope $2$, steeply up. At $y=-2$ it demands
                slope $-2$, steeply down. Getting further from the axis makes the segments steeper
                in both directions.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 2. Trace possible solution curves

        A slope field holds infinitely many solutions at once. An initial condition is what picks one
        out of the crowd: it says which point the curve has to pass through.

        Below, several exact solutions of $y'=y$ are laid over the field.
        """
    )
    return


@app.cell(hide_code=True)
def _(np, slope_field):
    _t = np.linspace(-3, 3, 400)
    _solutions = [(_t, _y0 * np.exp(_t), f'y(0) = {_y0}') for _y0 in [-2, -1, 0, 1, 2]]

    slope_field(lambda t, y: y, solutions=_solutions, title="y' = y with five solutions")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Observe

        The curves never cut across the segments. They ride along them. That is the whole
        relationship between a differential equation and its solutions, in one picture.

        Answer briefly:

        1. Which initial condition gives a constant solution, one that never moves?
        2. If $y(0) > 0$, does the solution rise or fall as $t$ increases?
        3. If $y(0) < 0$?

        Notice you answered all three off the picture. You never needed the formula $y = Ce^{t}$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Check yourself": mo.md(
                r"""
                (1) $y(0)=0$. The slope there is $0$, so the curve stays put forever. That is an
                **equilibrium solution**. (2) Rises, and faster and faster, because climbing puts it
                where the slopes are steeper. (3) Falls, and faster and faster, for the mirror-image
                reason.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 3. A parameter you can change: $y'=a-y$

        Here is a shape that shows up constantly, and for a reason. Newton's law of cooling, a drug
        clearing from the bloodstream, a bank balance drifting toward a target, all of them look like

        $$y'=a-y.$$

        Read it as a sentence too: *the rate of change is the gap between where you are and the level
        $a$*. Far from $a$, big gap, fast movement. Close to $a$, small gap, slow movement.

        Before you touch the slider, predict:

        - At what value of $y$ is the slope zero?
        - Above that value, do solutions rise or fall?
        - Below it?

        Now drag $a$ through several values.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    see_equilibrium = mo.ui.switch(
        value=False, label="Show the field, then drag $a$")
    see_equilibrium
    return (see_equilibrium,)


@app.cell(hide_code=True)
def _(mo):
    a = mo.ui.slider(start=-2.0, stop=4.0, step=0.5, value=1.0,
                     label="$a$", show_value=True)
    a
    return (a,)


@app.cell(hide_code=True)
def _(a, gated, see_equilibrium, slope_field):
    gated(
        see_equilibrium,
        lambda: slope_field(
            lambda t, y: a.value - y, t_range=(-3, 3), y_range=(-3, 5),
            title=f"y' = {a.value:.1f} - y   (equilibrium at y = {a.value:.1f})"),
    )
    return


@app.cell(hide_code=True)
def _(a, mo):
    mo.md(
        rf"""
        ### What changes, and what stays the same?

        Push the slider to both extremes on purpose. The whole flat row slides up and down with $a$,
        but the *behavior* around it never changes. Right now $a = {a.value:.1f}$, so the equilibrium
        sits at $y = {a.value:.1f}$, and every solution is being pulled onto that level.

        **In your notes,** fill these in:

        - The equilibrium sits where $y =$ \_\_\_\_\_\_\_\_.
        - Above the equilibrium, slopes are \_\_\_\_\_\_\_\_.
        - Below the equilibrium, slopes are \_\_\_\_\_\_\_\_.
        - So solutions are pushed \_\_\_\_\_\_\_\_ the equilibrium.

        That last one is what makes this a **stable equilibrium**: the field herds nearby solutions
        back toward it. Knock the system off the level $a$ and it returns on its own.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 4. When the slope depends on both variables

        Now something genuinely different:

        $$y'=t-y.$$

        Every field so far had parallel horizontal rows, because the slope only cared about $y$.
        Here the slope changes when you move sideways too.

        Before you look: the slope is zero where $t - y = 0$. What set of points in the
        $(t,y)$-plane is that? Say it before you flip the switch.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    see_nullcline = mo.ui.switch(
        value=False, label="Show the field for $y'=t-y$")
    see_nullcline
    return (see_nullcline,)


@app.cell(hide_code=True)
def _(gated, see_nullcline, slope_field):
    gated(
        see_nullcline,
        lambda: slope_field(lambda t, y: t - y, t_range=(-3, 3),
                            y_range=(-3, 3), density=25, title="y' = t - y"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Find the zero-slope line

        Hunt for the flat segments. They lie along the diagonal $y = t$.

        That line splits the plane into two regions, and the sign of $t-y$ tells you which way
        solutions move in each:

        - Below the line, $t - y > 0$, so slopes are positive and solutions climb.
        - Above the line, $t - y < 0$, so slopes are negative and solutions fall.

        A line like this, where the slope is zero, is called a **nullcline**, and finding one is
        often the first useful thing you can do with an equation you cannot solve. You just
        extracted the qualitative behavior of this ODE using nothing but algebra on $t - y = 0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 5. Predict a solution before you see it

        Take

        $$y'=t-y, \qquad y(0)=2.$$

        Using only the field above, predict:

        1. Is the slope at the starting point positive or negative?
        2. So does the solution start by moving up or down?
        3. Does it keep doing that forever, or does something change?

        Commit to an answer. Then reveal the curve.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    reveal = mo.ui.switch(value=False, label="Show the solution through $y(0)=2$")
    reveal
    return (reveal,)


@app.cell(hide_code=True)
def _(gated, reveal, slope_field, trace):
    def _draw():
        _f = lambda t, y: t - y
        _ts, _ys = trace(_f, t0=0.0, y0=2.0, t_range=(-3, 3))
        return slope_field(_f, t_range=(-3, 3), y_range=(-3, 4), density=25,
                           solutions=[(_ts, _ys, 'solution through y(0) = 2')],
                           title="y' = t - y,  y(0) = 2")

    gated(reveal, _draw,
          hint="Answer all three questions before you flip the switch.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Interpretation

        At $(0, 2)$ the equation demands slope $0 - 2 = -2$, so the curve starts down. But falling
        moves it into a region where $t - y$ is a different sign, and the field it meets there sends
        it back up.

        That reversal is worth sitting with. The equation never changed. The solution changed
        direction because it *moved*, and different places in the plane make different demands.

        Now compare that to what happens far to the right: the curve settles into a straight run
        parallel to the nullcline. Solutions of this equation forget where they started.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 6. Where does the initial condition take you?

        Same equation, but now you choose the starting point. Drag $y(0)$ from one end of the range
        to the other and watch the curve. Move $t_0$ too, to launch the curve from somewhere other
        than the vertical axis.

        Two things to look for:

        - Early on, curves starting at different heights look completely different.
        - Late on, they all do the same thing.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    y0 = mo.ui.slider(start=-3.0, stop=3.0, step=0.25, value=2.0,
                      label="$y(t_0)$", show_value=True)
    t0 = mo.ui.slider(start=-3.0, stop=3.0, step=0.25, value=0.0,
                      label="$t_0$", show_value=True)
    ghosts = mo.ui.checkbox(value=False, label="Overlay three neighboring starts")
    mo.vstack([y0, t0, ghosts])
    return ghosts, t0, y0


@app.cell(hide_code=True)
def _(ghosts, slope_field, t0, trace, y0):
    _f = lambda t, y: t - y

    _starts = [y0.value]
    if ghosts.value:
        _starts += [y0.value - 1.5, y0.value + 1.5, y0.value + 3.0]

    _sols = []
    for _s in _starts:
        _ts, _ys = trace(_f, t0=t0.value, y0=_s, t_range=(-3, 3))
        _sols.append((_ts, _ys, f'y({t0.value:.2f}) = {_s:.2f}'))

    slope_field(_f, t_range=(-3, 3), y_range=(-4, 4), density=25,
                solutions=_sols,
                title=f"y' = t - y,  y({t0.value:.2f}) = {y0.value:.2f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **In your notes:** describe in one sentence what all these solutions have in common for
        large $t$, even though they start in very different places.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Check yourself": mo.md(
                r"""
                They all converge onto the same straight line, $y = t - 1$, and run parallel to the
                nullcline. The initial condition controls the transient, the early wiggle, and then
                washes out. Whatever happens later has nothing to do with where you started.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 7. Final challenge: read the field cold

        Consider

        $$y'=y(2-y).$$

        This is the **logistic** equation, the standard model for a population with a ceiling: growth
        is fast when the population is small, and shuts off as it approaches the carrying capacity.

        Before you look, work out on paper:

        - Where are the equilibrium solutions? (Set $y(2-y)=0$.)
        - For $0 < y < 2$, are slopes positive or negative?
        - For $y > 2$?
        - For $y < 0$?
        - One of the two equilibria is stable and one is unstable. Which is which, and how will you
          tell from the picture?

        Then flip the switch and check. The slider drops a solution curve in at a starting height
        of your choosing, so you can test each of your four cases in turn.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    see_logistic = mo.ui.switch(
        value=False, label="Show the field, then drag the starting population")
    see_logistic
    return (see_logistic,)


@app.cell(hide_code=True)
def _(mo):
    p0 = mo.ui.slider(start=-1.0, stop=3.5, step=0.1, value=0.3,
                      label="starting population $y(0)$", show_value=True)
    p0
    return (p0,)


@app.cell(hide_code=True)
def _(gated, p0, see_logistic, slope_field, trace):
    def _draw():
        _f = lambda t, y: y * (2 - y)
        _ts, _ys = trace(_f, t0=0.0, y0=p0.value, t_range=(-3, 3))
        return slope_field(
            _f, t_range=(-3, 3), y_range=(-1.5, 3.5), density=25,
            solutions=[(_ts, _ys, f'y(0) = {p0.value:.1f}')],
            title=f"y' = y(2 - y),  y(0) = {p0.value:.1f}")

    gated(see_logistic, _draw,
          hint="Write down all five answers on paper before you flip the switch.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Check yourself once you have written your answers down": mo.md(
                r"""
                Equilibria at $y=0$ and $y=2$. Between them slopes are positive, so solutions climb
                toward $2$. Above $y=2$ slopes are negative, so those solutions fall back toward $2$.
                Below $y=0$ slopes are negative, so those run away downward.

                So $y=2$ is **stable**: arrows on both sides point toward it. $y=0$ is **unstable**:
                arrows on both sides point away. In population terms, the carrying capacity attracts
                and extinction repels, which is why a small population takes off rather than sitting
                still.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Sandbox: bring your own equation

        Type any expression in `t` and `y`. The field and a solution curve appear underneath.

        Things worth trying: `y - t**2`, `sin(t) - y`, `y*(1-y)*(y-2)`, `-t/y`, `t*y`.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    expr = mo.ui.text(value="sin(t) - y", label="y′ =", full_width=False)
    sb_y0 = mo.ui.slider(start=-4.0, stop=4.0, step=0.25, value=1.0,
                         label="$y(0)$", show_value=True)
    mo.vstack([expr, sb_y0])
    return expr, sb_y0


@app.cell(hide_code=True)
def _(expr, mo, np, sb_y0, slope_field, trace):
    _env = {n: getattr(np, n) for n in
            ('sin', 'cos', 'tan', 'exp', 'log', 'sqrt', 'abs', 'pi', 'tanh', 'arctan')}

    def _user_f(t, y):
        return eval(expr.value, {"__builtins__": {}}, {**_env, "t": t, "y": y})

    try:
        with np.errstate(all='ignore'):
            _ts, _ys = trace(_user_f, t0=0.0, y0=sb_y0.value, t_range=(-3, 3))
            _ys = np.where(np.abs(_ys) > 1e3, np.nan, _ys)
            _fig = slope_field(_user_f, t_range=(-3, 3), y_range=(-4, 4), density=25,
                               solutions=[(_ts, _ys, f'y(0) = {sb_y0.value:.2f}')],
                               title=f"y' = {expr.value}")
        _out = _fig
    except Exception as _e:
        _out = mo.callout(
            mo.md(f"Could not read `{expr.value}` as an expression in `t` and `y`.\n\n`{_e}`"),
            kind="warn",
        )
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Wrap-up

        You answered questions about stability, long-run behavior, and the effect of initial
        conditions for three different equations, and you did not solve a single one of them.

        That is the habit worth taking from here. Given

        $$y'=f(t,y),$$

        the sign and size of $f$ at a point tell you what a solution does there, and the places where
        $f = 0$ organize the whole picture. This scales: most differential equations that describe
        real systems cannot be solved in closed form, and this reasoning still works on every one of
        them.

        ### Exit question

        In two or three sentences, explain this statement in your own words:

        > A differential equation tells us how a solution moves locally, while a solution curve is
        > the accumulated result of following those local rules.

        If you can write that clearly, you have the idea.
        """
    )
    return


if __name__ == "__main__":
    app.run()
