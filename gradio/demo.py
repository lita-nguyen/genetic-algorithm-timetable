import gradio as gr
import pandas as pd

def preview_csvs(file1, file2):
    df1 = pd.read_csv(file1.name) if file1 else pd.DataFrame()
    df2 = pd.read_csv(file2.name) if file2 else pd.DataFrame()
    return df1, df2

with gr.Blocks() as demo:
    gr.Markdown("## 📚 Upload Timetabling Data")

    with gr.Row():
        file1_input = gr.File(label="📋 Teacher Schedule CSV", file_types=[".csv"])
        file2_input = gr.File(label="🎯 Student Wish CSV", file_types=[".csv"])

    with gr.Row():
        df1_output = gr.Dataframe(label="👩‍🏫 Teacher Schedule Preview", interactive=False, max_height=300)
        df2_output = gr.Dataframe(label="🙋 Student Wishes Preview", interactive=False, max_height=300)

    file1_input.change(fn=preview_csvs, inputs=[file1_input, file2_input], outputs=[df1_output, df2_output])
    file2_input.change(fn=preview_csvs, inputs=[file1_input, file2_input], outputs=[df1_output, df2_output])

demo.launch()