import gradio as gr
import cv2
import numpy as np

def butterworth_highpass_filter(image_shape, d0, n):
    """建立巴特沃斯高通濾波器遮罩"""
    rows, cols = image_shape
    crow, ccol = rows // 2, cols // 2
    u = np.arange(rows)
    v = np.arange(cols)
    u, v = np.meshgrid(u - crow, v - ccol, indexing='ij')
    d = np.sqrt(u**2 + v**2)
    # 巴特沃斯高通公式: 1 - 1/(1 + (D/D0)^(2n))
    h = 1 - 1 / (1 + (d / d0)**(2 * n))
    return h

def process_image(input_img, d0, n):
    if input_img is None:
        return None, "請上傳圖片"

    # 1. 灰階化與標準化 [cite: 17]
    gray = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)
    
    # 2. 二維離散傅立葉轉換 (2D DFT) [cite: 8]
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    
    # 3. 建立並套用巴特沃斯高通濾波器 [cite: 11]
    mask = butterworth_highpass_filter(gray.shape, d0, n)
    fshift_filtered = fshift * mask
    
    # 4. 為了視覺化：對數壓縮頻譜圖 [cite: 9]
    magnitude_spectrum = 20 * np.log(np.abs(fshift_filtered) + 1)
    magnitude_spectrum = np.uint8(cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX))

    # 5. 逆轉換回到空間域 (選做，可看濾波後的影像特徵)
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    img_back = np.uint8(cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX))

    return magnitude_spectrum, f"目前的參數設定：D0={d0}, n={n}。請 Member B 觀察高頻偽影是否明顯。"

# Gradio UI [cite: 19]
with gr.Blocks(title="AI 影像鑑識系統 - 實驗室版本") as demo:
    gr.Markdown("# 🧪 Week 2：頻率域特徵萃取實驗室")
    gr.Markdown("本介面供 **Member B** 調整巴特沃斯濾波器參數，以確立最佳偽影偵測組合 。")
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="上傳待測影像")
            # 參數控制區
            d0_slider = gr.Slider(minimum=1, maximum=200, value=30, step=1, label="截止頻率 (D0)")
            n_slider = gr.Slider(minimum=1, maximum=5, value=2, step=1, label="濾波器階數 (n)")
            run_btn = gr.Button("執行濾波分析", variant="primary")
        
        with gr.Column():
            output_fft = gr.Image(label="高通濾波後頻譜 (視覺化特徵)")
            status_text = gr.Textbox(label="系統狀態 / 參數紀錄")

    run_btn.click(
        fn=process_image, 
        inputs=[input_image, d0_slider, n_slider], 
        outputs=[output_fft, status_text]
    )

if __name__ == "__main__":
    demo.launch()
