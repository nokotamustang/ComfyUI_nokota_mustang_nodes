# ComfyUI Nokota Mustang nodes

I added my nodes that I am building for public use. I don't use any other nodes other than the default ones and these, so when I publish artwork with metadata you should be able to generate my work the same way.

Motivation: a lot of published nodes are created by people that aren't experienced programmers, let's say, or are making a complete dogs-dinner of code that should be much simpler in implementation. I also noticed a slow-down on startup with some packages out there so instead of complaining I just removed everything and created my own nodes. Last and largest point: I just wanted more features that are not available out there.

Post feedback or requests for nodes and features, I will be active in this area for a while.

![Screenshots](./screenshots/base_1.png)
_First three nodes available. The Random uINT makes a random unsigned integer on activation and you can store a lock value and toggle it when needed. The Dimension base attempts to simplify image size by providing an aspect ratio and a target mega pixel count. The Dimension multiplier simply allows scaling up of integer width and height dimensions._

The subsections will describe the nodes included in this repo.

Installation for now is simple, download the repo and copy the node folders into the `ComfyUI/custom_nodes` directory. I will work on adding this to the manager in the app soon.

## Dimension base

This node is my attempt to standardize image dimension sizes, I'm fed up of manually inputting values and having the default input fields clip or change the values, or just human error and inputting something off by a few pixels.

The drop down field will contain a fixed set of aspect ratios, and when the node is generated it will calculate the correct pixel width and height given the megapixel input.

I included the so to say standard ratios that relate to real world, but since some standards are fixed (say mostly in landscape) I make sure to add a portrait version (and vice-versa). I preferred this approach instead of creating a portrait or landscape flip node which seems too excessive.

The ratio is easy to understand, but take note of the target mega pixels input. This is a base value used to calculate the final dimension given your target ratio; if you wanted to create Full HD for example you can pick `Landscape HD (16:9)` and `2 million (base 1440 ~Full HD)`.

The stable diffusion base resolutions 512 and 1024 will be handy for creating base model images. I use `Landscape (3:2)` for my images right now, with target pixels to `1 million (SDXL base 1024)`; resulting in an image size of `1248 by 832`.

## Dimension multiplier

A simple node to take in a width and height and a scaler float, and produce a correct upscale. To produce the correctly rounded pixel sizes, ideally you want to provide a scale of 0.5, 1.5, 2.0, 4.0, 8.0, etc.

Given the example of `1248 by 832`, I am upscaling at 1.5 for a size of `1872 by 1248`. I can push 2.0x on my GPU if I don't do anything else during decoding, for a upscaled size of `1872 by 1248`.

This is handy for my purpose since I want to create a latent image with the base dimensions, and I want to feed the scaled up dimensions into the upscaler.

## Random uINT

My take on random integer generation since others either focus on providing negative integers (useless), are ~1000 lines long???, or don't work intuitively.

This node will generate a random unsigned integer. If you copy the random number into the lock value manually, you can lock the integer to this number if the lock switch is flipped on.

The number will generate on the node usage, so it's useful for seed generation and preserving the seed in the metadata for recreation.

