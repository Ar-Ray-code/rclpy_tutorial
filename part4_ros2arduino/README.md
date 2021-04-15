# EPS32 + ros2arduino (ROS2)の環境構築

　現在、ESP32をROSと連携させるために使えるros2arduinoはメインブランチのREADMEではDashingの対応が最新ですが、少し書き換えたところ、Foxyでも動作を確認しました。この記事では、その環境構築法の備忘録を書きます。後々のバージョンでFoxyの公式対応を待たなくてもESP32+ROS2を引き継ぐことができます。

- Ubuntu20.04 LTS & ROS2-Foxy
- ROS2のワークスペース：`~/ros2_ws/src`
- Arduinoのライブラリパス（Windowsでもコンパイル可）：`~/`

## Micro-XRCE-DDSのコンパイル

MicroXRCEDDSAgent (1.1.0)とros2arduino (0.2.1)の組み合わせを使うため、Micro-XRCE-DDSは過去のバージョンを使います。

```bash
$ cd ~
$ git clone https://github.com/eProsima/Micro-XRCE-DDS.git
$ cd Micro-XRCE-DDS/
$ git checkout v1.1.0
$ mkdir build
$ cd build
$ cmake ..
$ make
$ echo "MicroXRCEAgent='$(pwd)/MicroXRCEAgent'" >> ~/.bashrc
```

## ros2arduino（Foxy）のインストール

　次のリポジトリを使います。DashingとFoxyでは、std_msgsがexample_interfaces担っているので書き換えなければなりません。

[https://github.com/Ar-Ray-code/ros2arduino:embed:cite]

※ライブラリマネージャーからM5AtomとFastLEDのライブラリを、ボードマネージャーからESP32をインストールしておくこと

```bash
$ cd ~/Arduino/libraries/
$ git clone https://github.com/Ar-Ray-code/ros2arduino.git
$ git checkout 0.2.1_foxy
```

## shutdown_btnの導入（~/ros2_ws/src/以下）

　次のリポジトリを使います。

[https://github.com/Ar-Ray-code/M5AtomMatrix_playground:embed:cite]

```bash
$ cd　~/ros2_ws/src
$ git clone https://github.com/Ar-Ray-code/M5AtomMatrix_playground.git
$ cd M5AtomMatrix_playground/
$ git checkout foxy-devel
$ cd ../../
$ colcon build --symlink-install
```

## M5 Atom Matrixに書き込み

```bash
$ arduino ~/ros2_ws/src/M5AtomMatrix_playground/ROS2/shutdown_btn/m5atom_shutdown_btn_ros2/m5atom_shutdown_btn_ros2.ino
```

「ESP32 Pico Kit」を選択して、アップロードスピードを115200に設定して書き込みする。シリアルポートは`/dev/ttyUSB0`であった。

## Micro-XRCE-DDSの起動

M5AtomとPCをUSB接続して電源を入れます。Wi-Fi仕様に書き直せばWi-Fiでも動きます。。

```bash
$ MicroXRCEAgent serial --dev /dev/ttyUSB0
```

※topicは見えますが、nodeは見えません。

※2回リセットしないといけない場合があるので注意

```bash
$ source ~/.bashrc
$ ros2 topic echo /btn_msg
data: false
---
data: false
---
data: true
---
data: false
---
```

