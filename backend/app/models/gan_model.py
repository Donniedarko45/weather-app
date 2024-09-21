import tensorflow as tf
from tensorflow.keras.layers import Dense, LeakyReLU, Input
from tensorflow.keras.models import Sequential, Model
import numpy as np

# Generator model
def build_generator(latent_dim, output_dim):
    model = Sequential([
        Dense(128, input_dim=latent_dim),
        LeakyReLU(alpha=0.2),
        Dense(256),
        LeakyReLU(alpha=0.2),
        Dense(output_dim, activation='sigmoid')
    ])
    return model

# Discriminator model
def build_discriminator(input_dim):
    model = Sequential([
        Dense(256, input_dim=input_dim),
        LeakyReLU(alpha=0.2),
        Dense(128),
        LeakyReLU(alpha=0.2),
        Dense(1, activation='sigmoid')
    ])
    return model

# GAN model
def build_gan(generator, discriminator, latent_dim):
    discriminator.trainable = False
    gan_input = Input(shape=(latent_dim,))
    x = generator(gan_input)
    gan_output = discriminator(x)
    gan = Model(gan_input, gan_output)
    gan.compile(optimizer='adam', loss='binary_crossentropy')
    return gan

# Train the GAN
def train_gan(generator, discriminator, gan, data, latent_dim, epochs=10000, batch_size=32):
    for epoch in range(epochs):
        # Generate random noise for the generator
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        generated_data = generator.predict(noise)
        
        # Get a batch of real data
        real_data = data[np.random.randint(0, data.shape[0], batch_size)]
        
        # Train the discriminator
        discriminator.trainable = True
        d_loss_real = discriminator.train_on_batch(real_data, np.ones((batch_size, 1)))
        d_loss_fake = discriminator.train_on_batch(generated_data, np.zeros((batch_size, 1)))
        discriminator_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        
        # Train the generator
        discriminator.trainable = False
        generator_loss = gan.train_on_batch(noise, np.ones((batch_size, 1)))
        
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Discriminator Loss: {discriminator_loss}, Generator Loss: {generator_loss}")

# Initialize models
latent_dim = 100
output_dim = 784  # for MNIST dataset (28x28 = 784)

generator = build_generator(latent_dim, output_dim)
discriminator = build_discriminator(output_dim)
gan = build_gan(generator, discriminator, latent_dim)