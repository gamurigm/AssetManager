import os
import subprocess
import shutil

INPUT_DIR = r"C:\AssetManager\Finance_knowledge_base"
OUTPUT_DIR = r"C:\AssetManager\data\quant_kb"

MAPPING = {
    "A Linear Algebra Primer for Financial Engineering.pdf": "Math_and_Linear_Algebra",
    "Optimization Methods in Finance.pdf": "Optimization_Methods_v1",
    "Optimization Methods in Finance（second E）.pdf": "Optimization_Methods_v2",
    "Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005.pdf": "Stochastic_Calculus_I",
    "Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2).pdf": "Stochastic_Calculus_II",
    "financial-risk-modelling-and-portfolio-optimization-with-r-2nd-edt.pdf": "Risk_and_Portfolio_Optimization"
}

def main():
    quant_cli = r"C:\AssetManager\backend\venv\Scripts\quant-extractor.exe"
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for file_name in os.listdir(INPUT_DIR):
        if not file_name.endswith(".pdf"):
            continue
            
        file_path = os.path.join(INPUT_DIR, file_name)
        folder_name = MAPPING.get(file_name, "Uncategorized")
        target_dir = os.path.join(OUTPUT_DIR, folder_name)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        print(f"============== Processing: {file_name} ==============")
        print(f"Target: {target_dir}")
        subprocess.run([quant_cli, file_path, "-o", target_dir], shell=False)
        print("Done!\n")

if __name__ == "__main__":
    main()
