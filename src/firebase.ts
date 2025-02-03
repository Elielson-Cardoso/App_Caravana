import { initializeApp } from 'firebase/app';
import { getDatabase } from 'firebase/database';

const firebaseConfig = {
  databaseURL: "https://caravana-5fa6e-default-rtdb.firebaseio.com/",
  // Add other Firebase config here if needed
};

const app = initializeApp(firebaseConfig);
export const database = getDatabase(app);