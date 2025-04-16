import os
import subprocess
from pathlib import Path

def process_images():
    # 设置输入和输出目录
    input_dir = Path("/home/ubuntu/Projects/SHMT/Makeup-Wild/images/makeup")
    output_dir = Path(" /makeup")
    
    # 确保输出目录存在
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 获取所有图片文件
    image_files = list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png"))
    
    print(f"找到 {len(image_files)} 个图片文件")
    
    # 处理每个图片
    for img_path in image_files:
        print(f"处理图片: {img_path}")
        
        # 构建输出文件路径
        output_path = output_dir / f"{img_path.stem}_3d.jpg"
        
        # 构建命令
        cmd = [
            "python3", "demo.py",
            "-f", str(img_path),
            "-o", "pure_3d",
            "--show_flag", "false",
            "--mode", "gpu"
        ]
        
        # 执行命令
        try:
            subprocess.run(cmd, check=True)
            
            # 移动输出文件到目标目录
            if os.path.exists(f"examples/results/{img_path.stem}_pure_3d.jpg"):
                os.rename(
                    f"examples/results/{img_path.stem}_pure_3d.jpg",
                    str(output_path)
                )
                print(f"成功处理并保存: {output_path}")
            else:
                print(f"警告: 输出文件未找到: {img_path.stem}_pure_3d.jpg")
                
        except subprocess.CalledProcessError as e:
            print(f"处理图片 {img_path} 时出错: {e}")
        except Exception as e:
            print(f"处理图片 {img_path} 时发生未知错误: {e}")

if __name__ == "__main__":
    process_images() 