import { Box, FormControl, IconButton, InputLabel, Select, useTheme } from "@mui/material";
import { useContext, useState } from "react";
import { ColorModeContext, tokens } from "../../theme";
import InputBase from "@mui/material/InputBase";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";


import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
//import SearchIcon from "@mui/icons-material/Search";

const Topbar = () => {
  const pages = ['Dashboard', 'Details', 'Sensors', 'Compare'];
  const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const colorMode = useContext(ColorModeContext);

  const [project, setProject] = useState('');

  const handleChange = (event) => {
    setProject(event.target.value);
  };
  return (
    <Box display="flex" justifyContent="space-between" >
     
          <Typography
            variant="h6"
            fontSize={30}
            noWrap
            component="a"
            href="/"
            sx={{
              mt:1,
              ml:2,
              width:"150px",
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
              textAlign:"center"
            }}
          >
            EMAS
          </Typography>

        
          <Box
            //justifyContent={"space-around"} 
            sx={{ flexGrow: 1, display: { xs: 'flex', md: 'flex' } }}>
            {pages.map((page) => (
              <Button key={page} variant="h1"//onClick={""}
                sx={{ my: 1 }}
              >
                <Typography fontSize={15}>{page}</Typography>
              </Button>
              
            ))}
          </Box>
          <Box  my={1} minWidth={"100px"}>
              <FormControl fullWidth>
                <Select
                    fullWidth
                    displayEmpty
                    sx={{size:"small"}}
                    //labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={project}
                    //label="Project"
                    onChange={handleChange}
                  >
                    <MenuItem value={""}>Lok Ma Chau Loop Development Plan</MenuItem>
          
                    <MenuItem value={"project2"}>Project 2</MenuItem>
                    <MenuItem value={"project"}>Project 3</MenuItem>
                  </Select>
                </FormControl>
              </Box>
   
    
      {/* ICONS */}
      <Box display="flex">
        <IconButton onClick={colorMode.toggleColorMode}>
          {theme.palette.mode === "dark" ? (
            <DarkModeOutlinedIcon />
          ) : (
            <LightModeOutlinedIcon />
          )}
        </IconButton>
        
        <IconButton>
          <SettingsOutlinedIcon />
        </IconButton>
        <IconButton>
          <PersonOutlinedIcon />
        </IconButton>
      </Box>
    </Box>
  );
};

export default Topbar;


/*
 SEARCH BAR 
 <Box
 display="flex"
 backgroundColor={colors.primary[400]}
 borderRadius="3px"
>
 {/* <InputBase sx={{ ml: 2, flex: 1 }} placeholder="Search" />
 <IconButton type="button" sx={{ p: 1 }}>
 <SearchIcon /> 
 </IconButton> 
</Box>
{//<AdbIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
}


<Box sx={{ flexGrow: 0 }}>
  <Tooltip title="Open settings">
    <IconButton onClick={""}
      sx={{ p: 0 }}>
      <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
    </IconButton>
  </Tooltip>
  <Menu
    sx={{ mt: '45px' }}
    id="menu-appbar"
    anchorEl={""}
    anchorOrigin={{
      vertical: 'top',
      horizontal: 'right',
    }}
    keepMounted
    transformOrigin={{
      vertical: 'top',
      horizontal: 'right',
    }}
    open={Boolean("")}
    onClose={""}
  >
    {settings.map((setting) => (
      <MenuItem key={setting} onClick={""}>
        <Typography textAlign="center">{setting}</Typography>
      </MenuItem>
    ))}
  </Menu>
</Box>

*/