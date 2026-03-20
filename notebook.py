import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell
async def _():
    # Function to detect automatically if this is a webassembly notebook
    def is_webassembly_notebook():
        import sys
        return sys.platform == 'emscripten'

    # If it is a webassembly notebook install the package on the fly
    if is_webassembly_notebook():
        import micropip
        await micropip.install("graphviznb")
    return


@app.cell
def _():
    import graphviznb

    return (graphviznb,)


@app.cell
def _(graphviznb):
    w = graphviznb.Widget()
    w.source = """
    digraph {
        Hello -> World
        Hello -> Name
    }
    """
    w
    return


if __name__ == "__main__":
    app.run()
