import tensorflow as tf
import numpy as np
num_layers = 4

'''
input_data [n_steps, -1, num_units]
'''

def build_cell(rnn_size, name, isTrain):
    # 1、创建基本的lstm细胞核
    cell_fw = tf.nn.rnn_cell.BasicLSTMCell(num_units=rnn_size, name=name)
    if isTrain:
        keep_prob = 0.6
    else:
        keep_prob = 1.0
    drop = tf.nn.rnn_cell.DropoutWrapper(cell_fw, output_keep_prob=keep_prob)
    return drop

def convolutional(input_data, trainable, name, downsample=False, activate=True, bn=False, num_units=512):
    """
    通用的卷积操作
    :param input_data:
    :param filters_shape:
    :param trainable:
    :param name:
    :param downsample:
    :param activate:
    :param bn:
    :return:
    """
    with tf.variable_scope(name):
        if downsample and ('1111111times' in name):
            numTimes = 20
            idx = 0
            length = len(input_data)
            for i in range(0, numTimes):
                exec('temp{}=[]'.format(i))
            print(temp0)

            while idx < length:
                for i in range(0, numTimes):
                    exec('temp{}.append({})'.format(i, input_data[idx + i]))
                idx += 20

            outputs = []
            state_fwList = []
            state_bwList = []
            for i in range(0, numTimes):
                exec('drop_fw{} = tf.nn.rnn_cell.MultiRNNCell([build_cell({} // 2, name + {}, {}) for _ in range({})])'.format(i, num_units, i, trainable, num_layers))
                exec('drop_bw{} = tf.nn.rnn_cell.MultiRNNCell([build_cell({} // 2, name + {}, {}) for _ in range({})])'.format(i, num_units, i, trainable, num_layers))
                exec('birnn_outputs{}, state_fw{}, state_bw{} = tf.nn.static_bidirectional_rnn(cell_fw=drop_fw{}, cell_bw=drop_bw{}, inputs=temp{}, dtype=tf.float32)'.format(i, i, i, i, i, i))
                exec('outputs.append(birnn_outputs{}'.format(i))
                exec('state_fwList.append(state_fw{}'.format(i))
                exec('state_bwList.append(state_bw{}'.format(i))

            birnn_outputs = tf.reduce_mean(outputs, axis=0, keep_dims=False)
            state_fw = tf.reduce_mean(state_fwList, axis=0, keep_dims=False)
            state_bw = tf.reduce_mean(state_bwList, axis=0, keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        elif downsample and ('twentytimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            tempArray5 = []
            tempArray6 = []
            tempArray7 = []
            tempArray8 = []
            tempArray9 = []
            tempArray10 = []
            tempArray11 = []
            tempArray12 = []
            tempArray13 = []
            tempArray14 = []
            tempArray15 = []
            tempArray16 = []
            tempArray17 = []
            tempArray18 = []
            tempArray19 = []
            tempArray20 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                tempArray5.append(input_data[idx + 4])
                tempArray6.append(input_data[idx + 5])
                tempArray7.append(input_data[idx + 6])
                tempArray8.append(input_data[idx + 7])
                tempArray9.append(input_data[idx + 8])
                tempArray10.append(input_data[idx + 9])
                tempArray11.append(input_data[idx + 10])
                tempArray12.append(input_data[idx + 11])
                tempArray13.append(input_data[idx + 12])
                tempArray14.append(input_data[idx + 13])
                tempArray15.append(input_data[idx + 14])
                tempArray16.append(input_data[idx + 15])
                tempArray17.append(input_data[idx + 16])
                tempArray18.append(input_data[idx + 17])
                tempArray19.append(input_data[idx + 18])
                tempArray20.append(input_data[idx + 19])
                idx += 20

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_fw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_bw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_fw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_bw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_fw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_bw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_fw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_bw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_fw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_bw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_fw10 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '10', trainable) for _ in range(num_layers)])
            drop_bw10 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '10', trainable) for _ in range(num_layers)])
            drop_fw11 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '11', trainable) for _ in range(num_layers)])
            drop_bw11 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '11', trainable) for _ in range(num_layers)])
            drop_fw12 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '12', trainable) for _ in range(num_layers)])
            drop_bw12 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '12', trainable) for _ in range(num_layers)])
            drop_fw13 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '13', trainable) for _ in range(num_layers)])
            drop_bw13 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '13', trainable) for _ in range(num_layers)])
            drop_fw14 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '14', trainable) for _ in range(num_layers)])
            drop_bw14 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '14', trainable) for _ in range(num_layers)])
            drop_fw15 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '15', trainable) for _ in range(num_layers)])
            drop_bw15 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '15', trainable) for _ in range(num_layers)])
            drop_fw16 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '16', trainable) for _ in range(num_layers)])
            drop_bw16 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '16', trainable) for _ in range(num_layers)])
            drop_fw17 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '17', trainable) for _ in range(num_layers)])
            drop_bw17 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '17', trainable) for _ in range(num_layers)])
            drop_fw18 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '18', trainable) for _ in range(num_layers)])
            drop_bw18 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '18', trainable) for _ in range(num_layers)])
            drop_fw19 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '19', trainable) for _ in range(num_layers)])
            drop_bw19 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '19', trainable) for _ in range(num_layers)])
            drop_fw20 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '20', trainable) for _ in range(num_layers)])
            drop_bw20 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '20', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs5, state_fw5, state_bw5 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw5, cell_bw=drop_bw5, inputs=tempArray5, dtype=tf.float32)
            birnn_outputs6, state_fw6, state_bw6 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw6, cell_bw=drop_bw6, inputs=tempArray6, dtype=tf.float32)
            birnn_outputs7, state_fw7, state_bw7 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw7, cell_bw=drop_bw7, inputs=tempArray7, dtype=tf.float32)
            birnn_outputs8, state_fw8, state_bw8 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw8, cell_bw=drop_bw8, inputs=tempArray8, dtype=tf.float32)
            birnn_outputs9, state_fw9, state_bw9 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw9, cell_bw=drop_bw9, inputs=tempArray9, dtype=tf.float32)
            birnn_outputs10, state_fw10, state_bw10 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw10, cell_bw=drop_bw10, inputs=tempArray10, dtype=tf.float32)
            birnn_outputs11, state_fw11, state_bw11 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw11, cell_bw=drop_bw11, inputs=tempArray11, dtype=tf.float32)
            birnn_outputs12, state_fw12, state_bw12 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw12, cell_bw=drop_bw12, inputs=tempArray12, dtype=tf.float32)
            birnn_outputs13, state_fw13, state_bw13 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw13, cell_bw=drop_bw13, inputs=tempArray13, dtype=tf.float32)
            birnn_outputs14, state_fw14, state_bw14 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw14, cell_bw=drop_bw14, inputs=tempArray14, dtype=tf.float32)
            birnn_outputs15, state_fw15, state_bw15 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw15, cell_bw=drop_bw15, inputs=tempArray15, dtype=tf.float32)
            birnn_outputs16, state_fw16, state_bw16 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw16, cell_bw=drop_bw16, inputs=tempArray16, dtype=tf.float32)
            birnn_outputs17, state_fw17, state_bw17 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw17, cell_bw=drop_bw17, inputs=tempArray17, dtype=tf.float32)
            birnn_outputs18, state_fw18, state_bw18 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw18, cell_bw=drop_bw18, inputs=tempArray18, dtype=tf.float32)
            birnn_outputs19, state_fw19, state_bw19 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw19, cell_bw=drop_bw19, inputs=tempArray19, dtype=tf.float32)
            birnn_outputs20, state_fw20, state_bw20 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw20, cell_bw=drop_bw20, inputs=tempArray20, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4, birnn_outputs5, birnn_outputs6, birnn_outputs7, birnn_outputs8, birnn_outputs9, birnn_outputs10, birnn_outputs11, birnn_outputs12, birnn_outputs13, birnn_outputs14, birnn_outputs15, birnn_outputs16, birnn_outputs17, birnn_outputs18, birnn_outputs19, birnn_outputs20], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4, state_fw5, state_fw6, state_fw7, state_fw8, state_fw9, state_fw10, state_fw11, state_fw12, state_fw13, state_fw14, state_fw15, state_fw16, state_fw17, state_fw18, state_fw19, state_fw20], axis=0, keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4, state_bw5, state_bw6, state_bw7, state_bw8, state_bw9, state_bw10, state_bw11, state_bw12, state_bw13, state_bw14, state_bw15, state_bw16, state_bw17, state_bw18, state_bw19, state_bw20], axis=0, keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        elif downsample and ('eighteentimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            tempArray5 = []
            tempArray6 = []
            tempArray7 = []
            tempArray8 = []
            tempArray9 = []
            tempArray10 = []
            tempArray11 = []
            tempArray12 = []
            tempArray13 = []
            tempArray14 = []
            tempArray15 = []
            tempArray16 = []
            tempArray17 = []
            tempArray18 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                tempArray5.append(input_data[idx + 4])
                tempArray6.append(input_data[idx + 5])
                tempArray7.append(input_data[idx + 6])
                tempArray8.append(input_data[idx + 7])
                tempArray9.append(input_data[idx + 8])
                tempArray10.append(input_data[idx + 9])
                tempArray11.append(input_data[idx + 10])
                tempArray12.append(input_data[idx + 11])
                tempArray13.append(input_data[idx + 12])
                tempArray14.append(input_data[idx + 13])
                tempArray15.append(input_data[idx + 14])
                tempArray16.append(input_data[idx + 15])
                tempArray17.append(input_data[idx + 16])
                tempArray18.append(input_data[idx + 17])
                idx += 18

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_fw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_bw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_fw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_bw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_fw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_bw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_fw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_bw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_fw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_bw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_fw10 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '10', trainable) for _ in range(num_layers)])
            drop_bw10 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '10', trainable) for _ in range(num_layers)])
            drop_fw11 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '11', trainable) for _ in range(num_layers)])
            drop_bw11 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '11', trainable) for _ in range(num_layers)])
            drop_fw12 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '12', trainable) for _ in range(num_layers)])
            drop_bw12 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '12', trainable) for _ in range(num_layers)])
            drop_fw13 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '13', trainable) for _ in range(num_layers)])
            drop_bw13 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '13', trainable) for _ in range(num_layers)])
            drop_fw14 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '14', trainable) for _ in range(num_layers)])
            drop_bw14 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '14', trainable) for _ in range(num_layers)])
            drop_fw15 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '15', trainable) for _ in range(num_layers)])
            drop_bw15 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '15', trainable) for _ in range(num_layers)])
            drop_fw16 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '16', trainable) for _ in range(num_layers)])
            drop_bw16 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '16', trainable) for _ in range(num_layers)])
            drop_fw17 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '17', trainable) for _ in range(num_layers)])
            drop_bw17 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '17', trainable) for _ in range(num_layers)])
            drop_fw18 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '18', trainable) for _ in range(num_layers)])
            drop_bw18 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '18', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs5, state_fw5, state_bw5 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw5, cell_bw=drop_bw5, inputs=tempArray5, dtype=tf.float32)
            birnn_outputs6, state_fw6, state_bw6 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw6, cell_bw=drop_bw6, inputs=tempArray6, dtype=tf.float32)
            birnn_outputs7, state_fw7, state_bw7 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw7, cell_bw=drop_bw7, inputs=tempArray7, dtype=tf.float32)
            birnn_outputs8, state_fw8, state_bw8 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw8, cell_bw=drop_bw8, inputs=tempArray8, dtype=tf.float32)
            birnn_outputs9, state_fw9, state_bw9 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw9, cell_bw=drop_bw9, inputs=tempArray9, dtype=tf.float32)
            birnn_outputs10, state_fw10, state_bw10 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw10, cell_bw=drop_bw10, inputs=tempArray10, dtype=tf.float32)
            birnn_outputs11, state_fw11, state_bw11 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw11, cell_bw=drop_bw11, inputs=tempArray11, dtype=tf.float32)
            birnn_outputs12, state_fw12, state_bw12 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw12, cell_bw=drop_bw12, inputs=tempArray12, dtype=tf.float32)
            birnn_outputs13, state_fw13, state_bw13 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw13, cell_bw=drop_bw13, inputs=tempArray13, dtype=tf.float32)
            birnn_outputs14, state_fw14, state_bw14 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw14, cell_bw=drop_bw14, inputs=tempArray14, dtype=tf.float32)
            birnn_outputs15, state_fw15, state_bw15 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw15, cell_bw=drop_bw15, inputs=tempArray15, dtype=tf.float32)
            birnn_outputs16, state_fw16, state_bw16 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw16, cell_bw=drop_bw16, inputs=tempArray16, dtype=tf.float32)
            birnn_outputs17, state_fw17, state_bw17 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw17, cell_bw=drop_bw17, inputs=tempArray17, dtype=tf.float32)
            birnn_outputs18, state_fw18, state_bw18 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw18, cell_bw=drop_bw18, inputs=tempArray18, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4, birnn_outputs5, birnn_outputs6, birnn_outputs7, birnn_outputs8, birnn_outputs9, birnn_outputs10, birnn_outputs11, birnn_outputs12, birnn_outputs13, birnn_outputs14, birnn_outputs15, birnn_outputs16, birnn_outputs17, birnn_outputs18], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4, state_fw5, state_fw6, state_fw7, state_fw8, state_fw9, state_fw10, state_fw11, state_fw12, state_fw13, state_fw14, state_fw15, state_fw16, state_fw17, state_fw18], axis=0, keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4, state_bw5, state_bw6, state_bw7, state_bw8, state_bw9, state_bw10, state_bw11, state_bw12, state_bw13, state_bw14, state_bw15, state_bw16, state_bw17, state_bw18], axis=0, keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        elif downsample and ('tentimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            tempArray5 = []
            tempArray6 = []
            tempArray7 = []
            tempArray8 = []
            tempArray9 = []
            tempArray10 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                tempArray5.append(input_data[idx + 4])
                tempArray6.append(input_data[idx + 5])
                tempArray7.append(input_data[idx + 6])
                tempArray8.append(input_data[idx + 7])
                tempArray9.append(input_data[idx + 8])
                tempArray10.append(input_data[idx + 9])
                idx += 10

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_fw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_bw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_fw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_bw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_fw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_bw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_fw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_bw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_fw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_bw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_fw10 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '10', trainable) for _ in range(num_layers)])
            drop_bw10 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '10', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs5, state_fw5, state_bw5 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw5, cell_bw=drop_bw5, inputs=tempArray5, dtype=tf.float32)
            birnn_outputs6, state_fw6, state_bw6 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw6, cell_bw=drop_bw6, inputs=tempArray6, dtype=tf.float32)
            birnn_outputs7, state_fw7, state_bw7 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw7, cell_bw=drop_bw7, inputs=tempArray7, dtype=tf.float32)
            birnn_outputs8, state_fw8, state_bw8 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw8, cell_bw=drop_bw8, inputs=tempArray8, dtype=tf.float32)
            birnn_outputs9, state_fw9, state_bw9 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw9, cell_bw=drop_bw9, inputs=tempArray9, dtype=tf.float32)
            birnn_outputs10, state_fw10, state_bw10 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw10, cell_bw=drop_bw10, inputs=tempArray10, dtype=tf.float32)

            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4, birnn_outputs5, birnn_outputs6, birnn_outputs7, birnn_outputs8, birnn_outputs9, birnn_outputs10], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4, state_fw5, state_fw6, state_fw7, state_fw8, state_fw9, state_fw10], axis=0, keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4, state_bw5, state_bw6, state_bw7, state_bw8, state_bw9, state_bw10], axis=0, keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        elif downsample and ('ninetimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            tempArray5 = []
            tempArray6 = []
            tempArray7 = []
            tempArray8 = []
            tempArray9 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                tempArray5.append(input_data[idx + 4])
                tempArray6.append(input_data[idx + 5])
                tempArray7.append(input_data[idx + 6])
                tempArray8.append(input_data[idx + 7])
                tempArray9.append(input_data[idx + 8])
                idx += 9

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_fw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_bw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_fw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_bw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_fw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_bw7 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '7', trainable) for _ in range(num_layers)])
            drop_fw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_bw8 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '8', trainable) for _ in range(num_layers)])
            drop_fw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])
            drop_bw9 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '9', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs5, state_fw5, state_bw5 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw5, cell_bw=drop_bw5, inputs=tempArray5, dtype=tf.float32)
            birnn_outputs6, state_fw6, state_bw6 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw6, cell_bw=drop_bw6, inputs=tempArray6, dtype=tf.float32)
            birnn_outputs7, state_fw7, state_bw7 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw7, cell_bw=drop_bw7, inputs=tempArray7, dtype=tf.float32)
            birnn_outputs8, state_fw8, state_bw8 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw8, cell_bw=drop_bw8, inputs=tempArray8, dtype=tf.float32)
            birnn_outputs9, state_fw9, state_bw9 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw9, cell_bw=drop_bw9, inputs=tempArray9, dtype=tf.float32)

            birnn_outputs = tf.reduce_mean(
                [birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4, birnn_outputs5, birnn_outputs6,
                 birnn_outputs7, birnn_outputs8, birnn_outputs9], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean(
                [state_fw1, state_fw2, state_fw3, state_fw4, state_fw5, state_fw6, state_fw7, state_fw8, state_fw9], axis=0, keep_dims=False)
            state_bw = tf.reduce_mean(
                [state_bw1, state_bw2, state_bw3, state_bw4, state_bw5, state_bw6, state_bw7, state_bw8, state_bw9], axis=0, keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        elif downsample and ('sixtimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            tempArray5 = []
            tempArray6 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                tempArray5.append(input_data[idx + 4])
                tempArray6.append(input_data[idx + 5])
                idx += 6

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_fw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_bw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_fw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])
            drop_bw6 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '6', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs5, state_fw5, state_bw5 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw5, cell_bw=drop_bw5, inputs=tempArray5, dtype=tf.float32)
            birnn_outputs6, state_fw6, state_bw6 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw6, cell_bw=drop_bw6, inputs=tempArray6, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4, birnn_outputs5, birnn_outputs6], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4, state_fw5, state_fw6], axis=0,
                                           keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4, state_bw5, state_bw6], axis=0,
                                           keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        elif downsample and ('fivetimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            tempArray5 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                tempArray5.append(input_data[idx + 4])
                idx += 5

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_fw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])
            drop_bw5 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '5', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs5, state_fw5, state_bw5 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw5, cell_bw=drop_bw5, inputs=tempArray5, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4, birnn_outputs5], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4, state_fw5], axis=0,
                                           keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4, state_bw5], axis=0,
                                           keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])

        elif downsample and ('fourtimes' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            tempArray4 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                tempArray4.append(input_data[idx + 3])
                idx += 4

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4], axis=0,
                                           keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4], axis=0,
                                           keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])

        elif downsample and ('135' in name):
            tempArray1 = input_data[0: 135]
            tempArray2 = input_data[0: 45]
            tempArray2.extend(input_data[90: ])
            tempArray3 = input_data[0: 90]
            tempArray3.extend(input_data[135: ])
            tempArray4 = input_data[-135:]

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units//2, name + '3', trainable) for _ in range(num_layers)])
            drop_fw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])
            drop_bw4 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '4', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs4, state_fw4, state_bw4 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw4, cell_bw=drop_bw4, inputs=tempArray4, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3, birnn_outputs4], axis=0, keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3, state_fw4], axis=0,
                                      keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3, state_bw4], axis=0,
                                      keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])

        elif downsample and ('triple' in name):
            tempArray1 = []
            tempArray2 = []
            tempArray3 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                tempArray3.append(input_data[idx + 2])
                idx += 3

            drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw2 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '2', trainable) for _ in range(num_layers)])
            drop_fw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '3', trainable) for _ in range(num_layers)])
            drop_bw3 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '3', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw2, cell_bw=drop_bw2, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs3, state_fw3, state_bw3 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw3, cell_bw=drop_bw3, inputs=tempArray3, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2, birnn_outputs3], axis=0,
                                           keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2, state_fw3], axis=0,
                                      keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2, state_bw3], axis=0,
                                      keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])

        elif downsample and ('half' in name):
            tempArray1 = []
            tempArray2 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                tempArray2.append(input_data[idx + 1])
                idx += 2

            drop_fw21 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw21 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_fw22 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '2', trainable) for _ in range(num_layers)])
            drop_bw22 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '2', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw21, cell_bw=drop_bw21, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs2, state_fw2, state_bw2 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw22, cell_bw=drop_bw22, inputs=tempArray2, dtype=tf.float32)
            birnn_outputs = tf.reduce_mean([birnn_outputs1, birnn_outputs2], axis=0,
                                           keep_dims=False)
            state_fw = tf.reduce_mean([state_fw1, state_fw2], axis=0,
                                      keep_dims=False)
            state_bw = tf.reduce_mean([state_bw1, state_bw2], axis=0,
                                      keep_dims=False)
            outputs_return = []
            for i in range(birnn_outputs.shape[0]):
                outputs_return.append(birnn_outputs[i, :, :])
        else:
            tempArray1 = []
            idx = 0
            length = len(input_data)
            while idx < length:
                tempArray1.append(input_data[idx])
                idx += 1

            drop_fw31 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])
            drop_bw31 = tf.nn.rnn_cell.MultiRNNCell(
                [build_cell(num_units // 2, name + '1', trainable) for _ in range(num_layers)])

            birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
                cell_fw=drop_fw31, cell_bw=drop_bw31, inputs=tempArray1, dtype=tf.float32)
            birnn_outputs = birnn_outputs1
            state_fw = state_fw1
            state_bw = state_bw1
            outputs_return = birnn_outputs
    return outputs_return, state_fw, state_bw

def residual_block(input_data, trainable, name, num_units):
    #[90 -1 256]
    rnn_size = input_data[0].get_shape()[-1]
    short_cut = input_data
    with tf.variable_scope(name):
        #[90 -1 64]
        input_data = convolutional(input_data,
                                   trainable=trainable, name=name+'1', num_units=(rnn_size // 4))

        input_data = convolutional(input_data,
                                   trainable=trainable, name=name+'2', num_units=(rnn_size // 2))
        residual_output = input_data + short_cut
    return residual_output


def upsample(input_data, name, trainable, method="deconv", num_units=256):
    """
    数据上采样
    :param input_data:
    :param name:
    :param method:
    :return:
    """
    assert method in ["deconv", "tripleDeconv"]
    # tempZero = np.zeros(shape=tf.shape(input_data[0]))

    if method == "deconv":
        input_array = []
        idx = 0
        while idx < 2:
            # tempTensor1 = tf.get_variable(tempZero, dtype=tf.float32, name=name + ('tempTensor1_{}'.format(idx)))
            input_array.extend(input_data)
            # input_array.extend(tempTensor1)
            idx += 1
        drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
            [build_cell(num_units, name + '1', trainable) for _ in range(num_layers)])
        drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
            [build_cell(num_units, name + '1', trainable) for _ in range(num_layers)])

        birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
            cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=input_array, dtype=tf.float32)
        birnn_outputs = birnn_outputs1

    if method == "tripleDeconv":
        input_array = []
        idx = 0
        while idx < 3:
            # tempTensor1 = tf.get_variable(tempZero, dtype=tf.float32, name=name + ('tempTensor1_{}'.format(idx)))
            # tempTensor2 = tf.get_variable(tempZero, dtype=tf.float32, name=name + ('tempTensor2_{}'.format(idx)))
            input_array.extend(input_data)
            # input_array.extend(tempTensor1)
            # input_array.extend(tempTensor2)
            idx += 1
        drop_fw1 = tf.nn.rnn_cell.MultiRNNCell(
            [build_cell(num_units, name + '1', trainable) for _ in range(num_layers)])
        drop_bw1 = tf.nn.rnn_cell.MultiRNNCell(
            [build_cell(num_units, name + '1', trainable) for _ in range(num_layers)])

        birnn_outputs1, state_fw1, state_bw1 = tf.nn.static_bidirectional_rnn(
            cell_fw=drop_fw1, cell_bw=drop_bw1, inputs=input_array, dtype=tf.float32)
        birnn_outputs = birnn_outputs1
    return birnn_outputs