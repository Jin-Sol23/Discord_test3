import pandas as pd

# C_sample 엑셀 파일 불러오기
csample = 'C:/discord/230704 C_sample (text-chat).xlsx'
df = pd.read_excel(csample, sheet_name = 1)
print(df.head())

# dataframe명.shape : 행, 열의 개수를 튜플로 반환
print(df.shape) # (1048, 112)

print('ROI #', df.shape[1]) # 1열의 ROI 개수는 112개
print('time', df.shape[0]) # 총 1048분??

# 초당 프레임속도 (Frames per second, FPS)
# 프레임 = 각각의 정지 사진 하나
FPS = 4.3 # 1초에 4.3번 실행

# 프레임 수 계산??
print(df.shape[0] / FPS) # 243.72093....

