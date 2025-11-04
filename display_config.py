from IPython.display import display, HTML
import pandas as pd


def enable_clean_display():
    """Sets Pandas display options and injects CSS for clean, non-wrapping horizontal output."""

    # Pandas Options
    pd.set_option(
        'display.expand_frame_repr', False, # Stop wrapping and force scrolling
        'display.max_columns', None,        # Show all columns
        'display.width', 1000,              # Prevent wrapping
        'display.max_colwidth', 50          # Truncate extra-wide values
    )

    # Target plain-text output area and force horizontal scrolling.
    display(HTML("""<style>
    .jp-OutputArea-output pre {
        white-space: pre !important;
        word-break: keep-all !important;
        overflow-x: auto !important;}
    </style>"""))
