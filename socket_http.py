#!/usr/bin/env Python
# -*- coding:utf-8 -*-


import socket
import json


HOST = ''
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024


def start_http(sock):
    """开启http服务
    """
    while True:
        print('等待连接...')
        # 等待客户端连接,一直阻塞到客户端连接到
        conn, addr = sock.accept()
        print('成功连接： ', addr)
        try:
            # 接受客户端连接的数据，请求数据为 GET / HTTP/1.1
            data = conn.recv(BUFSIZE)
            if data:
                # 打印客户端的请求头
                print('客户端请求头：', data.decode('utf-8'))
                # 响应客户端的请求
                conn.sendall(build_response())
            # 关闭客户端的请求连接
            conn.close()
        except Exception as e:
            print(e)
            break


def build_response():
    """响应请求,响应数据为 HTTP/1.1 200 OK 空一行 加html文本
    """
    # 响应头和html文本之间空一行
    # response = f"""HTTP/1.1 200 OK

    #     <h1>this is a picture</h1>
    #     <img src="http://h.hiphotos.baidu.com/image/h%3D300/sign=a9f37a64f11f4134ff37037e151d95c1/c995d143ad4bd1137c1d50b556afa40f4afb0560.jpg" width="319.11357340720224" height="212.65927977839337">
    #     """.encode()  # 编码到bytes

    data = {
        'user': 'lcs',
        'passwd': '123'
    }
    json_data = json.dumps(data)
    # 响应字典数据，客户端取数据json.loads(response.content.decode('utf-8'))
    response = f"""HTTP/1.1 200 OK

        {json_data}
        """.encode('utf-8')
    return response


def main():
    # 新建socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP相关参数

    # 绑定地址
    sock.bind(ADDR)

    # 监听连接个数
    sock.listen(1)

    print('启动http')
    start_http(sock)


if __name__ == '__main__':
    main()