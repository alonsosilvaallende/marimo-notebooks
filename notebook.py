import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import graphviznb

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
