import React from 'react';
import { motion } from 'framer-motion';

const Animation = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '40px' }}>
      <motion.div
        animate={{
          scale: [1, 1.2, 1],
          rotate: [0, 180, 360],
          borderRadius: ["20%", "50%", "20%"]
        }}
        transition={{
          duration: 2,
          ease: "easeInOut",
          times: [0, 0.5, 1],
          repeat: Infinity,
        }}
        style={{
          width: 80,
          height: 80,
          backgroundColor: 'var(--primary-orange)',
          boxShadow: '0 0 20px rgba(255, 126, 39, 0.5)'
        }}
      />
      <motion.h3
        animate={{ opacity: [0.5, 1, 0.5] }}
        transition={{ duration: 1.5, repeat: Infinity }}
        style={{ marginTop: '20px', color: 'var(--primary-green)' }}
      >
        Analyzing Performance Data...
      </motion.h3>
    </div>
  );
};

export default Animation;
