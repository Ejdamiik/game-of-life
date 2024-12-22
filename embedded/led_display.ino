#include "display.h"
#include <SPI.h>
#include <vector>

// Pin definitions for MAX7219
const int DIN_PIN = 23;  // Data In
const int CS_PIN = 5;   // Chip Select
const int CLK_PIN = 18;  // Clock

const int WIDTH = 32;
const int HEIGHT = 8;

// Initialize the LedControl library
// Parameters: DataIn, Clock, Load(CS), Number of MAX7219 devices
ExtendedDisplay display = ExtendedDisplay(DIN_PIN, CLK_PIN, CS_PIN, 4);

std::vector< std::vector<bool> > grid = {};

void setup()
{
  // Initialize the MAX7219 device
  display.shutdown(false);       // Wake up the MAX7219 from power-saving mode
  display.setIntensity(8);       // Set brightness level (0 is min, 15 is max)
  display.clearDisplay();          // Clear the display

  for ( int i = 0; i < HEIGHT; i++ )
  {
    std::vector<bool> row = {};
    for ( int j = 0; j < WIDTH; j++ )
    {
      row.push_back(false);
    }
    grid.push_back(row);
  }

  for ( int i = 4; i < 7; i++ )
  {
    for ( int j = 8; j < 14; j++ )
    {
      grid[i][j] = true;
    }
  }

  for ( int i = 1; i < 3; i++ )
  {
    for ( int j = 4; j < 8; j++ )
    {
      grid[i][j] = true;
    }
  }

}

void updateDisplay()
{
  for ( int i = 0; i < HEIGHT; i++ )
  {
    for ( int j = 0; j < WIDTH; j++ )
    {
      display.setLed(i, j, grid[i][j]);
    }
  }
}

int living( int i, int j )
{
  int res = 0;
  for ( int di = -1; di <= 1; di++ )
  {
    for ( int dj = -1; dj <= 1; dj++ )
    {
      if ( di != 0 || dj != 0 )
      {
        int ni = (i + di + HEIGHT) % HEIGHT;
        int nj = (j + dj + WIDTH) % WIDTH;
        if ( grid[ni][nj] )
        {
          res++;
        }
      }
    }
  }
  return res;
}

void evolve()
{
  std::vector< std::vector<bool> > nw_grid = grid;
  for ( int i = 0; i < HEIGHT; i++ )
  {
    for ( int j = 0; j < WIDTH; j++ )
    {
      int alive = living( i, j );
      if ( grid[i][j] )
      {
        if (alive < 2 || alive > 3)
        {
          nw_grid[i][j] = false;
        }
      }
      else
      {
        if ( alive == 3 )
        {
          nw_grid[i][j] = true;
        }
      }
    }
  }

  grid = nw_grid;

}

void loop()
{
  updateDisplay();
  evolve();
  delay( 500 );
}
