#!/bin/bash

# Build script for Vercel deployment
echo "Building Django project for Vercel..."

# Collect static files
python manage.py collectstatic --noinput

echo "Build completed successfully!"