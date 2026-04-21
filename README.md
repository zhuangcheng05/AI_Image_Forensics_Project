# AI_Image_Forensics_Project
# Week 1 任務指南：基礎設施搭建與介面原型
**負責人**：Member C (系統與全端工程師)
**本週目標**：建立團隊共用的程式碼倉庫、配置開發環境，並產出第一版可運行的 Gradio 網頁原型。

---

## 1. 建立 GitHub 協作倉庫 (Repository)

GitHub 是團隊同步程式碼的核心樞紐。

1. **新建倉庫**：登入 GitHub，建立一個名為 `AI_Image_Forensics_Project` 的公開或私有倉庫。
2. **邀請成員**：進入倉庫的 `Settings` > `Collaborators`，輸入 Member A 與 Member B 的 GitHub 帳號並發送邀請。
3. **建立環境清單**：在倉庫根目錄下新建 `requirements.txt` 檔案，寫入本專案所需之核心套件：
   ```text
   gradio
   opencv-python
   numpy
   scikit-learn
