import gradio as gr
import pandas as pd

reset_tab_style = """
<style>
.tabs {
    gap: 0!important;
}

.tabs .tab-wrapper {
    padding-bottom: 0!important;
}

.tabs .tab-container[role="tablist"] { 
    display: flex;
    position: relative;
    flex-wrap: wrap;
    border-bottom: 1px solid var(--border-color-primary);
    overflow: unset;
}

.tabs .tab-wrapper .tab-container:after {
    content: none;
}

.tabs button[role="tab"] {
    margin-bottom: -2px;
    border: 1px solid transparent;
    border-color: transparent;
    border-bottom: none;
    border-top-right-radius: var(--container-radius);
    border-top-left-radius: var(--container-radius);
    padding: var(--size-1) var(--size-4);
    color: var(--body-text-color-subdued);
    font-weight: var(--section-header-text-weight);
    font-size: var(--section-header-text-size);
}

.tabs button[role="tab"].selected {
    border-color: var(--border-color-primary);
    background: var(--background-fill-primary);
    color: var(--body-text-color);
}

.tabs button[role="tab"]:after,
.tabs button[role="tab"].selected:after {
    content: none;
}

.tabs .tabitem {
    position: relative;
    border: 1px solid var(--border-color-primary);
    border-top: none;
    border-bottom-right-radius: var(--container-radius);
    border-bottom-left-radius: var(--container-radius);
    padding: var(--block-padding);
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>
"""


def preview_csvs(file1, file2):
    df1 = pd.read_csv(file1.name) if file1 else pd.DataFrame()
    df2 = pd.read_csv(file2.name) if file2 else pd.DataFrame()
    return df1, df2


with gr.Blocks() as demo:
    gr.HTML(reset_tab_style)
    gr.Markdown(
        """
        <h1 style="text-align: center;">Timetabling App</h1>
        <p style="text-align: center; margin-top: 0;">Môn: Cục xì lầu</p>
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Tabs():
                with gr.Tab("Course Schedule"):
                    file1_input = gr.File(label="CSV Upload", file_types=[".csv"])
                    df1_output = gr.Dataframe(
                        label="📁 Preview",
                        interactive=False,
                        max_height=300,
                    )
                with gr.Tab("Student Wishes"):
                    file2_input = gr.File(label="CSV Upload", file_types=[".csv"])
                    df2_output = gr.Dataframe(
                        label="📁 Preview",
                        interactive=False,
                        max_height=300,
                    )

            with gr.Row():
                gr.Button(variant="primary", value="Gen timetable")
                gr.ClearButton()

        with gr.Column(scale=2):
            with gr.Tabs():
                with gr.Tab("Timetable"):
                    gr.Markdown(
                        "### 📖 Upload a CSV file to preview the course schedule."
                    )

        with gr.Column(scale=1):
            with gr.Tabs():
                with gr.Tab("File to Demo"):
                    gr.Gallery(
                        value=[
                            "https://github.com/lita-nguyen/genetic-algorithm-timetable/blob/main/data/courses.csv",
                            "https://github.com/lita-nguyen/genetic-algorithm-timetable/blob/main/data/students.csv",
                        ],
                        file_types=[".csv"],
                        label="📁 Example CSV Files",
                    )

    file1_input.change(
        fn=preview_csvs,
        inputs=[file1_input, file2_input],
        outputs=[df1_output, df2_output],
    )
    file2_input.change(
        fn=preview_csvs,
        inputs=[file1_input, file2_input],
        outputs=[df1_output, df2_output],
    )

demo.launch()
