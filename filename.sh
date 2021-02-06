#!/bin/bash

gksudo 'fdisk -l' | sed -n '/^[/]/p' | awk '{print $1}';