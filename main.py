import os
import subprocess
# Function to generate LaTeX code
def generate_latex_code(N, M):
    latex_code = r"""
\documentclass[12pt, a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{ctex}
\usepackage{titlesec}
\titleformat{\chapter}
{\normalfont\Large\bfseries}{\thechapter}{1em}{}
\begin{document}
	
	\begin{titlepage}
		
		% 标题
		\title{报告标题}
		\author{作者姓名}
		\date{\today}
		
		% 添加一个居中的Logo或图片
		\begin{center}
%			\includegraphics[width=0.5\textwidth]{logo.png} % 替换为你的Logo文件路径
		\end{center}
		
		% 报告标题部分
		\vspace{2cm}
		\begin{center}
			\textbf{\Huge 报告标题}
		\end{center}
		
		% 作者和日期部分
		\vfill
		\begin{center}
			\textbf{\Large 作者姓名}
		\end{center}
		\vspace{0.5cm}
		\begin{center}
			\textbf{\large \today}
		\end{center}
		
		% 底部可以添加额外信息
		\vfill
		\begin{center}
			\textbf{\small 额外信息或部门名称}
		\end{center}
		
	\end{titlepage}
	\tableofcontents
	\chapter{简介}

    \chapter{前雷达}
"""

    # Loop through sections (1 to N)
    for n in range(1, N + 1):
        latex_code += f"\section{{T-{n}}}\n"
        
        # Loop through subsections (1 to M) for each section
        for m in range(1, M + 1):
            subsection = f"T-{n}-{m}"
            # figure_path = f"fig/T_{n}/T_{n}_{m}/fig.png"
            latex_code += f"\subsection{{{subsection}}}\n"
            latex_code += r"\begin{figure}[h!]" + "\n"
            latex_code += r"\centering" + "\n"
            # latex_code += f"\includegraphics[width=0.8\textwidth]{{{figure_path}}}" + "\n"
            latex_code += r"\caption{Your caption here.}" + "\n"
            latex_code += r"\end{figure}" + "\n"

    latex_code += r"\end{document}"

    return latex_code

# Define the values for N and M
N = 3  # Number of sections
M = 2  # Number of subsections per section

# Generate LaTeX code
latex_code = generate_latex_code(N, M)

# Write LaTeX code to a .tex file
tex_file = "generated_document.tex"
with open(tex_file, "w") as f:
    f.write(latex_code)

print(f"LaTeX file has been written to {tex_file}")


subprocess.run(["xelatex", tex_file], check=True)
subprocess.run(["xelatex", tex_file], check=True)
