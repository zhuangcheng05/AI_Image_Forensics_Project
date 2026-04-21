import gradio as gr
import cv2
import numpy as np

# 這是未來放置你隊友 (Member B) 濾波邏輯的地方
def detect_ai_generated(input_img):
    # 目前先回傳原圖，證明網頁有在運作
    return input_img, "等待模型整合中..."

# 建立 Gradio 網頁介面佈局
with gr.Blocks(title="AI 影像鑑識系統") as demo:
    gr.Markdown("# 揭露隱形的破綻：AI 生成影像鑑識系統")
    
    with gr.Row():
        # 左側：上傳區
        with gr.Column():
            input_image = gr.Image(label="上傳待測影像")
            run_btn = gr.Button("開始鑑定")
        
        # 右側：結果顯示區
        with gr.Column():
            output_features = gr.Image(label="高頻頻譜特徵 (FFT)")
            result_text = gr.Textbox(label="鑑定結果")

    # 設定按鈕按下去會發生什麼事
    run_btn.click(
        fn=detect_ai_generated, 
        inputs=input_image, 
        outputs=[output_features, result_text]
    )

# 啟動網頁
if __name__ == "__main__":
    # 決定你要怎麼開店 (二選一)：
    
    # 做法 A：產生公開連結，可以丟給組員看 (有效期限 72 小時)
    demo.launch(share=True) 
    
    # 做法 B：如果你只想在自己電腦上看，就把上面那行刪掉，改成下面這行：
    # demo.launch()
