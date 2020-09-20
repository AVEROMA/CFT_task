import matplotlib.pyplot as plt
import librosa.display
import os


def do_task():
    path = '/home/averoma/PycharmProjects/CFT_task/uploads'
    dst = '/home/averoma/PycharmProjects/CFT_task/static/images/spectrogram.png'

    # Сортируем файлы по времени изменения, чтобы взять последний добавленный файл
    file_list = os.listdir(path)
    full_list = [os.path.join(path, i) for i in file_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)

    x, sr = librosa.load(time_sorted_list[0])
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.savefig(dst)
