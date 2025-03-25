
#speed 
## RNNs
is a cyclic connection, tendo a capacidade de atualizar o estado atual baseado nos estados passados e no input data atual. 
- Problema: quando tem um gap muito grande no  input data relevante, as RNNs de cima não conseguem conectar na informação relevante.
- Para resolver esse problema, foi criada **LSTM -  Long Short-term Memory**

Nas RNNs, as recurrent layers são recurrent cells na qual os estados são afetados pelos states passados e também pelo input atual com feedback connections. 

**Standard Recurrent Cell:** sigma cells, o padrão da RNNs, porém tem o problema de memoria

## LSTM
Para resolver esse problema foi criado a LSTM cells.
Essas cells melhoram a capacidade de lembrar das cells, por meio da introdução de um "gate" na cell. 

- **LSTM without Forget Gate:** When updating the cell state, the input gate can decide what new information can be stored in the cell state, and the output gate decides what information can be output based on the cell state.
- **LSTM with Forget Gate:** The forget gate can decide what information will be thrown away from the cell state. When the value of the forget gate, f t , is 1, it keeps this information; meanwhile, a value of 0 means it gets rid of all the information.
	- increasing the bios of the forget gate increases the performance of the LSTM network
- **LSTM with a Peephole Connection:** As the gates of the above LSTM cells do not have direct connections from the cell state, there is a lack of essential information that harms the network’s performance. *The peephole connections* permite a LSTM cell ver os estados internos atuais e isso faz com que, as células possam aprender stable and precise timing algorithms sem aprender forçadamente.
- **Gated Recurrent Unit:** a capacidade de aprendizado da célula LSTM é maior do que as normais de RNN, porém possui um custo computacional adicional, que é o parâmetro adicional.
	- Logo, para diminuir esse custo computacional, *GRU* integra o input + output gate da célula LSTM, como um *update gate*. Formando uma célula com somente dois gates, update and reset.
	- É como uma célula com forget gates
	- Por possuir -1 parâmetro, a GRU is less powerful than the original LSTM, so it cannot work with context-free language and translation


## Networks
All RNNs pode ser modificada as LSTM Networks, mudando a recurrente cell para a LSTM cell.
**LSTM-dominated network:** neural networks that are mainly built with LSTM cells, focusing on optimizing the connections of the inner LSTM cells, para melhorar as propriedades da rede.

- **Stacked LSTM Network:** stack of LSTM layers, most basic, a multilayer fully connected structure. These output-input connections are the only relation between two adjacent layers.
	- used to solver vehicle-to-vehicle communication
	- translation
- **Bidirectional LSTM Network:** Traditional RNN are only able to make use of a previous context, but this Bidirectional arch could be trained in both time directions simultaneous with hidden separate layers (forward and backwards ex). 
	- sequence-based prediction of protein localization
- **Multidimensional LSTM Network:** build as many recurrent connections as th dimensions of the data. At each point in the data sequence, the recurrent layer L receives both the output of layer L − 1 and its own activations from one step back along all dimensions. This means that the LSTM cells in layer L have n-forget gates in the n-dimensional LSTM network (one for each of the cell’s previous states along every dimension). 
- **Graph LSTM Network:** The graph LSTM model assumes that each superpixel node is defined by its previous states and adaptive neighboring nodes. 