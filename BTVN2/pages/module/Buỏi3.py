from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

# Đường dẫn đến file âm thanh
fileName = 'C:\\Users\\User\\Desktop\\DocumentUni\\XLTHS\\bai3.wav'

try:
    # Đọc file âm thanh
    samplerate, data = wavfile.read(fileName)

    
    # Nhập giá trị M từ người dùng
    M = 2

    # Tăng tần số lẫy mẫu (up-sampling) bằng zero-padding : ví dụ data = [1,2,3]  sau khi repeat thành [1,1,2,2,3,3]
    upsampled_data = np.repeat(data, M)

    # Giảm tần số lẫy mẫu (down-sampling) bằng cách chỉ giữ lại 1 mẫu trong M mẫu liên tiếp ví dụ data[1,2,3,4,5,6] thành [1.3.5]
    downsampled_data = upsampled_data[::M]


    sd.play(data, samplerate)
    sd.wait()

    # Vẽ biểu đồ tín hiệu ban đầu
    stepSize = np.arange(len(data)) / samplerate
    plt.figure(figsize=(12, 10))
    plt.subplot(3, 1, 1)
    plt.plot(stepSize, data)
    plt.ylabel('Biên độ')
    plt.xlabel('Thời gian (s)')
    plt.title('Âm thanh gốc')

    # Vẽ biểu đồ tín hiệu up-sampled
    stepSize_upsampled = np.arange(len(upsampled_data)) / (samplerate * M)
    plt.subplot(3, 1, 2)
    plt.plot(stepSize_upsampled, upsampled_data)
    plt.ylabel('Biên độ')
    plt.xlabel('Thời gian (s)')
    plt.title('Âm thanh tăng tần số')

    # Vẽ biểu đồ tín hiệu down-sampled
    stepSize_downsampled = np.arange(len(downsampled_data)) / (samplerate)
    plt.subplot(3, 1, 3)
    plt.plot(stepSize_downsampled, downsampled_data)
    plt.ylabel('Biên độ')
    plt.xlabel('Thời gian (s)')
    plt.title('Âm thanh giảm tần số')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"File '{fileName}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
