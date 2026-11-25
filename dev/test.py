import os
os.environ["KERAS_BACKEND"] = "torch"
import keras

mnist = keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Sequential API
model = keras.models.Sequential([
  keras.layers.Input(shape=(28, 28)),
  keras.layers.Flatten(),
  keras.layers.Dense(512, activation='relu'),
  keras.layers.Dropout(0.2),
  keras.layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=5)

# evaluate model
model.evaluate(x_test, y_test)

# Same model with the functional API
inputs = keras.Input(shape=(28, 28))
x = keras.layers.Flatten()(inputs)
x = keras.layers.Dense(512, activation='relu')(x)
x = keras.layers.Dropout(0.2)(x)
outputs = keras.layers.Dense(10, activation='softmax')(x)
model = keras.Model(inputs=inputs, outputs=outputs)

# Examples of common layers (not used above)

# dense (fully connected)
dense = keras.layers.Dense(
    units=128,                          # number of neurons (output size)
    activation='relu',                  # default: None (linear)
    use_bias=True,                      # default: True
    kernel_initializer='glorot_uniform',# default: 'glorot_uniform'
    bias_initializer='zeros',           # default: 'zeros'
    kernel_regularizer=None,            # default: None, e.g. keras.regularizers.L2(0.01)
    bias_regularizer=None,              # default: None
    activity_regularizer=None,          # default: None (penalty on the layer output)
    kernel_constraint=None,             # default: None, e.g. keras.constraints.MaxNorm(3)
    bias_constraint=None,               # default: None
)

# dropout: randomly sets 30% of the inputs to 0 during training
dropout = keras.layers.Dropout(0.3)

# pooling
maxpool = keras.layers.MaxPooling2D(pool_size=(2, 2))
avgpool = keras.layers.AveragePooling2D(pool_size=(2, 2))
globalpool = keras.layers.GlobalAveragePooling2D()

# convolution
conv2d = keras.layers.Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu')
conv1d = keras.layers.Conv1D(16, kernel_size=5, activation='relu')

# recurrent
rnn = keras.layers.SimpleRNN(32)
lstm = keras.layers.LSTM(64, return_sequences=True)
gru = keras.layers.GRU(64)



